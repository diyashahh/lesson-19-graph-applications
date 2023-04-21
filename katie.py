# Using Kruskal's

# Problem: What is the minimum number of steps you can take to get to every house in your neighborhood.
#
# Use Kruskals but add a counter to keep track of weighted edges kept by kruskals algorithim. 
#
import networkx as nx;
import matplotlib.pyplot as plt;

kruskals_neighborhood = nx.Graph()
kruskals_neighborhood.add_weighted_edges_from(BranchList)
prog = 'neato'
root = None
# pos = nx.nx_pydot.graphviz_layout(G,prog,root)
pos = nx.nx_pydot.pydot_layout(kruskals_neighborhood)
plt.figure()    
nx.draw(G,pos,edge_color='black',width=1,linewidths=1, node_size=10,node_color='blue',alpha=0.9)
plt.axis('on')
plt.show()



