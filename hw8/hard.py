#learnt how to get networks and run it from the easy py, had to do this in myenv python /home/ubuntu/data5500_mycode/hw8/hard.py
#import networkx as nx
import networkx as nx
#create function that takes a graph and sees how many nodes have a degree greater than 5
def count_nodes_with_degree_greater_than_5(graph):
    # Count nodes with degree greater than 5
    #Graph.nodes gets all the nodes in the graph, graph.degree(node) returns the degree or number of connections/edges of a node
    return sum(1 for node in graph.nodes if graph.degree(node) > 5)

# Example
G = nx.Graph() #create this empty graph yay
#asked chat to help with getting nodes with degree higher than 5
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),  # Node 1 has degree 6 which helped me understand more what we were looking for in terms of degree
                  (2, 3), (3, 4), (4, 5), (5, 6), (6, 7),  
                  (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8)]) 
# Add additional edges to make some nodes have a degree greater than 5 so we can test it works
#I wanted to see each node to make sure this was working, and to see what each node's degree was, I was curious I guess
for node in G.nodes:
    print(f"Node {node} has degree {G.degree(node)}")
#output of how many have a degree higher than 5
print(count_nodes_with_degree_greater_than_5(G))  
