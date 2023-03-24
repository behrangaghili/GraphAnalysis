import networkx as nx
import matplotlib.pyplot as plt
# Read the Facebook social network
G = nx.read_edgelist("facebook_combined.txt")

# compute the metrics
num_nodes = len(g.nodes())
num_edges = len(g.edges())
avg_degree = sum([val for (node, val) in g.degree()]) / float(num_nodes)
density = nx.density(g)
diameter = max([max(j.values()) for (i,j) in nx.shortest_path_length(g)])
diameter = nx.diameter(g.to_undirected())
avg_clustering = nx.average_clustering(g)
transitivity = nx.transitivity(g)
avg_shortest_path_length = nx.average_shortest_path_length(g)

print(f"number of nodes: {num_nodes}")
print(f"number of edges: {num_edges}")
print(f"average degree: {avg_degree:.2f}")
print(f"density: {density:.4f}")
print(f"diameter: {diameter}")
print(f"average clustering coefficient: {avg_clustering:.4f}")
print(f"transitivity: {transitivity:.4f}")
print(f"average shortest path length: {avg_shortest_path_length:.2f}")



 # compute assortativity
assortativity = nx.degree_assortativity_coefficient(g)
print(f"assortativity (degree correlation): {assortativity:.4f}")

 # compute degree centrality
deg_cen = nx.degree_centrality(g)

 # compute betweenness centrality
bet_cen = nx.betweenness_centrality(g)

 # compute closeness centrality
clo_cen = nx.closeness_centrality(g)

 # compute pagerank centrality
pg_cen = nx.pagerank(g)

 # find top 5 nodes for each metric
top5_deg_cen = sorted(deg_cen, key=deg_cen.get, reverse=true)[:5]
top5_bet_cen = sorted(bet_cen, key=bet_cen.get, reverse=true)[:5]
top5_clo_cen = sorted(clo_cen, key=clo_cen.get, reverse=true)[:5]
top5_pg_cen = sorted(pg_cen, key=pg_cen.get, reverse=true)[:5]

 #print the results
print("top 5 nodes based on degree centrality:")
print(top5_deg_cen)
print("top 5 nodes based on betweenness centrality:")
print(top5_bet_cen)
print("top 5 nodes based on closeness centrality:")
print(top5_clo_cen)
print("top 5 nodes based on pagerank centrality:")
print(top5_pg_cen)

 # compute network centralization based on the four metrics
deg_cen_vals = list(deg_cen.values())
bet_cen_vals = list(bet_cen.values())
clo_cen_vals = list(clo_cen.values())
pg_cen_vals = list(pg_cen.values())

max_deg_cen = max(deg_cen_vals)
max_bet_cen = max(bet_cen_vals)
max_clo_cen = max(clo_cen_vals)
max_pg_cen = max(pg_cen_vals)


#print network centralization
print("max degree =", max_deg_cen)
print("max betweenness=", max_bet_cen)
print("max closeness=",max_clo_cen )
print("max pagerank = ",max_pg_cen )

centralization_deg = sum([max_deg_cen - x for x in deg_cen_vals]) / ((num_nodes - 1) * (num_nodes - 2))
centralization_bet = sum([max_bet_cen - x for x in bet_cen_vals]) / ((num_nodes - 1) * (num_nodes - 2))
centralization_clo = sum([max_clo_cen - x for x in clo_cen_vals]) / ((num_nodes - 1) * (num_nodes - 2))
centralization_pg = sum([max_pg_cen - x for x in pg_cen_vals]) / ((num_nodes - 1) * (num_nodes - 2))

print("network centralization based on degree centrality:", centralization_deg)
print("network centralization based on betweenness centrality:", centralization_bet)
print("network centralization based on closeness centrality:" , centralization_clo)
print("network centralization based on pagerank centrality:" , centralization_pg)
print("dr aliakbari thanks a lot for teaching us new thing")


# Plot degree distribution
degrees = [val for (node, val) in G.degree()]
plt.hist(degrees, bins=50)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()
print("Dr ALiakbari Thanks a lot for teaching us new thing")