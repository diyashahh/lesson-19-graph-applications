import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
nodes = ["A","B","C","D","E","F","G","H"
                  ,"I","J","K","L","M","N","O","P",
                  "R","S","T"]
g.add_nodes_from(nodes)


g.add_edge("I", "O")
g.add_edge("O", "C")
g.add_edge("P", "O")
g.add_edge("A", "O")
g.add_edge("B", "O")
g.add_edge("E", "M")
g.add_edge("D", "E")
g.add_edge("N", "D")
g.add_edge("C", "N")
g.add_edge("I", "C")
g.add_edge("I", "S")
g.add_edge("J", "I")
g.add_edge("K", "J")
g.add_edge("G", "H")
g.add_edge("F", "G")
g.add_edge("F", "D")
g.add_edge("F", "I")
g.add_edge("G", "J")
g.add_edge("H", "K")
g.add_edge("R", "M")
g.add_edge("K", "L")
g.add_edge("A", "S")
g.add_edge("B", "N")
g.add_edge("T", "B")
g.add_edge("T", "E")
g.add_edge("T", "R")
g.add_edge("P", "R")
g.add_edge("P", "L")
g.add_edge("M", "K")
g.add_edge("P", "L")
g.add_edge("F", "I")
g.add_edge("R", "E")
g.add_edge("P", "D")
g.add_edge("M", "L")

pos = nx.fruchterman_reingold_layout(g)

nx.draw_networkx_edge_labels(g,pos, edge_labels = {('A', 'S'):'Short St',
    ('I', 'O') : 'High St',
    ('O', 'C') : 'Adams Rd',
    ('O', 'P') : 'Laurel Ave',
    ('A', 'O') : 'Choate St',
    ('O', 'B') : 'Academy St',
    ('B','T') : 'Haines St',
    ('E', 'M') : 'Chapel St',
    ('D', 'E') : 'Clover Ln',
    ('N','D') : 'Day Dr',
    ('C', 'N') : 'East Dr',
    ('I', 'C'): 'West Dr',
    ('I', 'S') : 'Grove St',
    ('J', 'I'):'Kings Dr' ,
    ('K', 'J') : 'Pine Rd',
    ('G', 'H') : 'North St',
    ('F','G') : 'South St',
    ('D','F') : 'Wood Ln',
    ('F', 'I') : 'Rose Rd',
    ('G','J') : 'Stone St',
    ('H','K') : 'Sparks Ave',
    ('R', 'M') : 'Daisy Rd',
    ('K','L') : 'Strong St',
    ('L','P') : 'Fire Ave',
    ('B','N') : 'Long St',
    ('E', 'T'): 'Fly Dr',
    ('P', 'R'): 'Train Ln',
    ('P', 'D'): 'Low St',
    ('E', 'R'): 'Sky St',
    ('T', 'R'): 'Main St',
    ('L', 'M'): 'Velvet Dr'}
    , font_color = "blue", label_pos = .5,rotate = True, font_size=5, font_weight = "bold")
nx.draw_networkx(g, pos, with_labels=True,node_color="blue",node_size=700, font_color="white", font_size=7)

plt.savefig("Ana_graph")
plt.margins(0.1)
plt.show()

print(list(nx.edge_dfs(g,'A')))

