#Import networkx and requests for graphing and getting the api
import networkx as nx
import requests

#Get the exchange rates from the API
def fetch_exchange_rates():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,eos&vs_currencies=eth,btc,ltc,xrp,ada,btc,eos"
    response = requests.get(url)
    return response.json()

# Create a graph from the exchange rates
def create_graph(exchange_data):
    g = nx.DiGraph()  
    
    # Add edges with the weights being the exchange rates
    for currency, rates in exchange_data.items():
        for target_currency, rate in rates.items():
            if rate != 0:  # So you only add edges with a valid exchange rate
                g.add_edge(currency, target_currency, weight=rate)
    
    #print the graph to verify
    #print(f"Graph Nodes: {g.nodes}")
    #print(f"Graph Edges: {g.edges(data=True)}")
    
    return g

#Calculate the path weight by multiplying edge weights along the path
def calculate_path_weight(g, path):
    weight = 1.0
    for i in range(len(path) - 1):
        weight *= g[path[i]][path[i + 1]]['weight']
    return weight

#Find all paths between two nodes
def find_all_paths(g, node1, node2):
    try:
        return list(nx.all_simple_paths(g, node1, node2))
    except nx.NetworkXNoPath:
        return []

#Check for arbitrage opportunities by calculating reverse paths
#Got help from chat on this, just to kind of figure out how to reverse the paths and see the weights
def check_arbitrage(g, node1, node2):
    paths_to = find_all_paths(g, node1, node2)
    paths_from = find_all_paths(g, node2, node1)

    max_factor = 1.0
    min_factor = 1.0
    max_path = []
    min_path = []

    for path_to in paths_to:
        weight_to = calculate_path_weight(g, path_to)
        for path_from in paths_from:
            weight_from = calculate_path_weight(g, path_from)
            factor = weight_to * weight_from

            if factor > max_factor:
                max_factor = factor
                max_path = (path_to, path_from)

            if factor < min_factor:
                min_factor = factor
                min_path = (path_to, path_from)
    #I could not figure out how to get the max and min paths, and the right arbitrages, I tried several different things but couldn't figure it out
    return max_factor, max_path, min_factor, min_path

def main():
    #Get the real-time exchange rates
    exchange_data = fetch_exchange_rates()
    #print("Exchange Data: ", exchange_data)  #Test print

    # Create the graph
    g = create_graph(exchange_data)

    # Print all paths and their weight 
    for node1 in g.nodes:
        for node2 in g.nodes:
            if node1 != node2:
                paths_to = find_all_paths(g, node1, node2)
                paths_from = find_all_paths(g, node2, node1)

                if paths_to or paths_from:
                    print(f"\nPaths from {node1} to {node2}:")
                    for path_to in paths_to:
                        weight_to = calculate_path_weight(g, path_to)
                        print(f"Path: {path_to} -> Weight: {weight_to}")
                    for path_from in paths_from:
                        weight_from = calculate_path_weight(g, path_from)
                        print(f"Reverse Path: {path_from} -> Weight: {weight_from}")

    #Find arbitrage opportunities
    max_factor, max_path, min_factor, min_path = check_arbitrage(g, 'eos', 'ltc')
    print(f"\nMax Arbitrage Factor: {max_factor} -> Path: {max_path}")
    print(f"Min Arbitrage Factor: {min_factor} -> Path: {min_path}")

#Run the program chat helped me tie all the functions together with main()
if __name__ == "__main__":
    main()
