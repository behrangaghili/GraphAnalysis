import networkx as nx
import matplotlib.pyplot as plt
import sys


    
# Load the graph from the dataset
G = nx.read_edgelist("cit-HepTh.txt",comments="#",delimiter="\t", create_using=nx.DiGraph(),nodetype=int )

# Compute the basic network properties
num_nodes = len(G.nodes())
num_edges = len(G.edges())
avg_degree = sum([val for (node, val) in G.degree()]) / float(num_nodes)
# density = nx.density(G)
#As the graph is not connected, I am reporting here the largest computed diameter among the connected components.
#The commented code below gets an exception "Found infinite path length because the graph is not connected"
#Therefore, I used the connected component with the maximum diameter.
#diameter = nx.diameter(G.to_undirected())
# diameter = max([max(j.values()) for (i,j) in nx.shortest_path_length(G)])
# avg_clustering = nx.average_clustering(G)
# transitivity = nx.transitivity(G)
# avg_shortest_path_length = nx.average_shortest_path_length(G)

# print(f"Number of nodes: {num_nodes}")
# print(f"Number of edges: {num_edges}")
# print(f"Average degree: {avg_degree:.2f}")
# print(f"Density: {density:.4f}")
# print(f"Diameter: {diameter}")
# print(f"Average clustering coefficient: {avg_clustering:.4f}")
# print(f"Transitivity: {transitivity:.4f}")
# print(f"Average shortest path length: {avg_shortest_path_length:.2f}")

# # Compute assortativity
# assortativity = nx.degree_assortativity_coefficient(G)
# print(f"Assortativity (Degree Correlation): {assortativity:.4f}")

# compute centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
pagerank_centrality = nx.pagerank(G)

# # Print top 5 nodes based on each centrality measure
def print_top_k_centrality(centrality, k, name):
    sorted_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {k} nodes by {name}:")
    for i in range(k):
        print(f"{sorted_nodes[i][0]}: {sorted_nodes[i][1]:.4f}")
    print()
    
# print_top_k_centrality(degree_centrality, 5, "degree centrality")
# print_top_k_centrality(betweenness_centrality, 5, "betweenness centrality")
# print_top_k_centrality(closeness_centrality, 5, "closeness centrality")
# print_top_k_centrality(pagerank_centrality, 5, "PageRank centrality")

# Compute network centralization
max_degree = max([val for (node, val) in G.degree()])
max_betweenness = max(betweenness_centrality.values())
max_closeness = max(closeness_centrality.values())
max_pagerank = max(pagerank_centrality.values())
degree_centralization = sum([(max_degree - val) for (node, val) in G.degree()]) / float((num_nodes - 1) * (num_nodes - 2))
betweenness_centralization = sum([(max_betweenness - val) for (node, val) in betweenness_centrality.items()]) / float((num_nodes - 1) * (num_nodes - 2))
closeness_centralization = sum([(max_closeness - val) for (node, val) in closeness_centrality.items()]) / float((num_nodes - 1) * (num_nodes - 2))
pagerank_centralization = sum([(max_pagerank - val) for (node, val) in pagerank_centrality.items()]) / float((num_nodes - 1) * (num_nodes - 2))

# Print network centralization
print(f"max degree =", max_degree)
print("max betweenness=", max_betweenness)
print("max closeness=",max_closeness )
print("max pagerank = ",max_pagerank )
print("degree centralization = ",degree_centralization )
print("betweenness centralization = ",betweenness_centralization )
print("closeness centralization = ",closeness_centralization )
print("pagerank centralization = ",pagerank_centralization )

# # Plot degree distribution
# degrees = [val for (node, val) in G.degree()]
# plt.hist(degrees, bins=50)
# plt.title("Degree Distribution")
# plt.xlabel("Degree")
# plt.ylabel("Frequency")
# plt.show()

