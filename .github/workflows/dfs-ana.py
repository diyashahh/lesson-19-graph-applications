import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_nodes_from(["Short St","High St","Adams Rd","Laurel Ave","Choate St","Academy St","Haines St","Chapel St"
                  ,"Clover Ln","Day Dr","East Dr","West Dr","Grove St","Kings Dr","Pine Rd","North St",
                  "South St","Wood Ln","Rose Rd","Stone St","Sparks Ave","Night Dr"])


g.add_edges_from([("Short St", "Pine Rd"), ("Short St", "Rose Rd"), ("High St", "Pine Rd"), ("High St", "South St"), ("High St", "Kings Dr"),
                ("Adams Rd", "Kings Dr"), ("Adams Rd", "Clover Ln"), ("Adams Rd", "Pine Rd"), ("Laurel Ave", "Choate St"), ("Laurel Ave", "Academy St"),
                ("Laurel Ave", "Kings Dr"), ("Choate St", "Sparks Ave"), ("Academy St", "Haines St"), ("Academy St", "Clover Ln"), 
                ("Haines St", "Chapel St"), ("Haines St", "Day Dr"), ("Chapel St", "West Dr"), 
                ("Clover Ln", "Day Dr"),("Clover Ln", "Rose Rd"), ("Clover Ln", "Pine Rd"), ("Day Dr", "Academy St"), ("Day Dr", "West Dr"),
                ("East Dr", "Chapel St"), ("East Dr", "Day Dr"), ("West Dr", "Night Dr"), ("West Dr", "North St"), 
                ("Grove St", "Wood Ln"), ("Grove St", "Choate St"), ("Grove St", "Night Dr"), ("Pine Rd", "North St"), ("North St", "Academy St"), 
                ("North St", "Wood Ln"), ("South St", "High St"), ("South St", "Wood Ln"), ("South St", "Choate St"), ("Wood Ln", "Pine Rd"), 
                ("Wood Ln", "Sparks Ave"), ("Rose Rd", "Academy St"), ("Stone St", "Pine Rd"), 
                ("Night Dr", "Academy St"), ("Night Dr", "Sparks Ave"), ("Sparks Ave", "Grove St")])

# Graph represented as an alphabetic list
graph = {
    'A': ['O', 'S'],
    'B': ['O', 'T', 'N'],
    'C': ['N', 'I', 'O'],
    'D': ['E', 'F', 'N'],
    'E': ['M', 'T', 'D'],
    'F': ['D', 'G', 'I'],
    'G': ['F', 'H', 'J'],
    'H': ['G', 'K'],
    'I': ['C', 'J', 'S', 'O'],
    'J': ['I', 'K', 'G'],
    'K': ['H', 'J'],
    'L': ['V', 'P'],
    'M': ['R', 'E', 'V'],
    'N': ['D', 'C', 'B'],
    'O': ['C', 'A', 'P', 'B'],
    'P': ['L', 'R', 'O'],
    'Q': ['B', 'R', 'E'],
    'R': ['P', 'M', 'Q'],
    'S': ['I', 'A'],
    'T': ['L', 'K'],
    'U': ['P', 'O'],
    'V': ['L', 'M']
}

visited = set() # Set to keep track of visited nodes.


def dfs(graph, node, visited):
    
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

nx.draw_networkx(g, with_labels=True,node_color="blue",node_size=700, font_color="white", font_size=5)
plt.margins(0)
plt.show()

dfs(visited, graph, 'A')

