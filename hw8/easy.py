#The first step in this assignment was getting networkx to work which was an insane hassle, I ended up asking chat gpt over and over again how to get it downloaded
#eventually it had me do myenv which is a virtual environment so I could download and use netowrkx
#ran it with (myenv) ip/path ... python /home/ubuntu/data5500_mycode/hw8/easy.py 
#then just ran deactivate to get out of virtual myenv
#Import Networkx as nx like in the graphing video
import networkx as nx
#Create a function to count the nodes, using len and graph.nodes to give access to all the nodes in the graph
def count_nodes(graph):
    return len(graph.nodes)

# Example 
G = nx.Graph() # empty graph
G.add_edges_from([(1, 2), (2, 3), (3, 4)]) #adds angles and nodes 1, 2, 3, 4, to the graph
print(count_nodes(G))  # Output should be 4
