
import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt



house_nums = [[1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [5, 19], [6, 8], [7, 9], 
         [7, 10], [8, 11], [9, 12], [10, 13], [11, 14], [11, 15], [12, 16], 
         [13, 17], [15, 18], [15, 19], [16, 20], [18, 21], [19, 21], [20, 5], 
         [21, 2],[17,9],[19,10],[14,10],[12,8],[10,12],[1,3],[2,19],[16,8]]

G = nx.Graph()
G.add_edges_from(house_nums)
pos = nx.spring_layout(G,seed=4)
fig = plt.figure(figsize=(14, 8)) # set the figure size
fig.text(0.5, 0.95, "Kim's Neighborhood", fontsize=14, ha='center')
fig.text(0.5, 0.9, "Is the neighborhood connected: {}".format(nx.is_connected(G)), fontsize=10, ha='center')




nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=400, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(1, 2): 'Main St.', 
                 (2, 3): 'Elm St.', 
                 (2, 4): 'Oak St.', 
                 (4, 5): 'Maple Ave.', 
                 (4, 6): 'Cherry Ln.', 
                 (5, 19): 'Cedar St.', 
                 (6, 8): 'Pine St.', 
                 (7, 9): 'Spruce Rd.', 
                 (7, 10): 'Birch Rd.', 
                 (8, 11): 'Holly Dr.', 
                 (9, 12): 'Juniper Ln.', 
                 (10, 13): 'Dogwood Dr.', 
                 (11, 14): 'Magnolia Ave.', 
                 (11, 15): 'Cypress Rd.', 
                 (12, 16): 'Fir Ct.', 
                 (13, 17): 'Azalea St.', 
                 (15, 18): 'Garden Way', 
                 (15, 19): 'Star St.', 
                 (16, 20): 'Sycamore Pl.', 
                 (18, 21): 'Rose Ln.', 
                 (19, 21): 'Vine St.', 
                 (20, 5): 'Poplar Ave.', 
                 (21, 2): 'Oak St.',
                 (17,9): 'Slay St.',
                 (19,10): 'Hello St.',
                 (14,10): 'World St.',
                 (12,8): 'Flag St.',
                 (10,12): 'Rock St.',
                 (1,3): 'Party Ct.',
                 (2,19): 'Globe St.',
                 (16,8): 'Sun Ln.',

                 },
    font_color='purple',
    font_size=8
)
plt.show()
print(nx.is_connected(G))