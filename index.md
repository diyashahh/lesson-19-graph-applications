# Title of Your Project

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:
* Diya Shah (diyashah@udel.edu)
* Rana Tuncer (rantun@udel.edu)
* Katie Oates (email)
* Ana (email)

Description of project

## Installation Code

```sh
$> pip install networkx
```

## Python Environment Setup

```python
import networkx as nx
```

# First Problem Title

**Informal Description**:
Beth Brown has recently been elected as a community representative. With her new role, she has to visit different families and ask them about life in the neighborhood. However, a lot of people have questions for Beth and often stop her to ask about improvements for the neighborhood, which tires her out quite a bit!

Today Beth has decided to visit the Koch household; what path will ensure that Beth gets asked the least amount of questions on the way from her house (Brown) to the Kochs?

> **Formal Description**:
> Beth's house and her community can be represented with a weighted, undirected graph; each vertex of the graph is a household or outdoor venue in the neighborhood, and each weighted edge connecting two vertices is the amount of questions Beth gets asked on her way from one location to another.

> Using Dijkstra's algorithm, we can find the shortest path from Beth's house to the Koch's house--the shortest path being the one with which Beth gets asked the least number of questions.

>  * Input: A graph of 20 vertices (labelled with last names of each household/name of outdoor spot) and 25 edges (labelled with weights representing number of questions)
>  * Output: A list of vertices representing the path from Beth's house to the Koch household

> *Note: Edges with a weight greater than 7 are colored red to indicate high value paths for easier visuals)*

**Graph Problem/Algorithm**: SSSP - Dijkstra's Algorithm


**Setup code**:

```python
import matplotlib.pyplot as plt
from random import randint
```

**Visualization**:

![Graph of Beth's Neighborhood](/bethgraph.png)

**Solution code:**

```python
G = nx.Graph()
verts = ['Brown','Smith','park','Singh',"O'Neil",'Lewis','pond','Adebe','Patel','Koch',
        'Uysal','creek','Jones','Khan','Keen','Baird','forest','Zeng','Davis', 'Garcia']
G.add_nodes_from(verts)

# Add random weighted edges between vertices
G.add_weighted_edges_from([('Brown','Adebe', 15),
                            ('Brown','Baird', 6),
                            ('Brown','Zeng',11),
                            ('Smith','O\'Neil', 6),
                            ('park','Keen', 10),
                            ('park','forest', 8),
                            ('park','Uysal', 12),
                            ('Singh','O\'Neil', 3),
                            ('Singh','Jones', 3),
                            ('Singh','forest', 5),
                            ('O\'Neil','Koch', 11),
                            ('Lewis','Baird', 7),
                            ('pond','Keen', 4),
                            ('pond','Adebe', 3),
                            ('pond','Lewis', 2),
                            ('Adebe','creek', 2),
                            ('Adebe', 'Khan', 7),
                            ('Patel','Khan', 15),
                            ('Jones','Garcia', 4),
                            ('Jones','creek', 1),
                            ('forest', 'Zeng', 5),
                            ('Koch','Davis', 9),
                            ('Khan','Keen', 6),
                            ('Keen','Baird', 14),
                            ('Davis','Garcia', 8)])

# Color edges depending on weight
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 7]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 7]

# Draw graph
pos= nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='orange')

# Draw edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, edge_color="red", style="dotted", width=2)
nx.draw_networkx_edges(G, pos, edgelist=esmall, style="dotted", width=2)

# Draw weights of edges
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight) 

# Show graph
plt.show(G)

# Find the shortest path between nodes using Dijkstra's algorithm
shortest_path = nx.dijkstra_path(G, 'Brown', 'Koch')
print(shortest_path)
```

**Output**

```python
['Brown', 'Zeng', 'forest', 'Singh', "O'Neil", 'Koch']
```

**Interpretation of Results**:
The shortest path from Beth's house to the Koch residency involves traversing the path from the Zeng household, the forest, Singh household, and O'Neil household, before finally reaching the Koch's house. Using this path, the total number of questions Beth would receive on her way is 35.




# Problem 2: Kim Just Moved in
**Informal Description**: 
Kim recently moved into house number 1 in a new neighborhood, and she wants to meet all her neighbors! She wants to see if she would be able to visit all her neighbors within the neighborhood (by checking if the neighborhood is connected). Additionally, she wants to organize the houses by levels in the neighborhood, so that she can easily remember which neighbors live in what part of the neighborhood.

> **Formal Description**:
>  * Input: A graph of 21 nodes and 31 edges - edges labelled with street names, nodes labelled with house numbers.
>  * Output: (String) Strings letting the user know if the graph is connected, and lists of the grouped nodes in each level (boolean and lists that I converted to string for ease)



**BFS Algorithm**


**Setup code**:

```python
import networkx as nx
import matplotlib.pyplot as plt
```

**Visualization**:

![Kim's Neighborhood](/Kim_Graph.png)

**Solution code:**
```python
import networkx as nx
import matplotlib.pyplot as plt

house_nums = [[1, 2], [2, 3], [2, 4], [4, 5], [4, 6], [5, 19], [6, 8], [7, 9], 
         [7, 10], [8, 11], [9, 12], [10, 13], [11, 14], [11, 15], [12, 16], 
         [13, 17], [15, 18], [15, 19], [16, 20], [18, 21], [19, 21], [20, 5], 
         [21, 2],[17,9],[19,10],[14,10],[12,8],[10,12],[1,3],[2,19],[16,8]]

G = nx.Graph()
G.add_edges_from(house_nums)
layout = nx.spring_layout(G,seed=4) # so its the same graph each time I run the code
fig = plt.figure(figsize=(14, 8)) # set the figure size
fig.text(0.5, .96, "Kim's Neighborhood", fontsize=14 ,ha='center')
fig.text(0.5, 0.92, "Is the neighborhood connected: {}".format(nx.is_connected(G)), fontsize=10, ha='center')
fig.text(0.5, 0.9, "Nodes represent house numbers, Edges represent streets", fontsize=8, ha='center')


nx.draw(
    G, layout, edge_color='black', width=1, linewidths=1,
    node_size=400, node_color='pink', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw_networkx_edge_labels(
   #adding street names
    G, layout,
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
plt.savefig("Kim_Graph")
plt.show()
print("Is the neighborhood connected: " + str(nx.is_connected(G)))
print("These are the houses in each level, each list represents a level:")
for layer in nx.bfs_layers(G,1):
    print(str(layer))

```

**Output**

Is the neighborhood connected: True <br>   

These are the houses in each level, each list represents a level: <br>   

[1]
[2, 3]
[4, 21, 19]
[5, 6, 18, 15, 10]
[20, 8, 11, 7, 13, 14, 12]
[16, 9, 17]

**Interpretation of Results**:
The BFS algorithm is used to traverse a graph in a breadth-first manner, i.e., visiting all the nodes at a given level before moving to the next level. In this case, the BFS algorithm is used to determine if it is possible for Kim to visit all her neighbors without leaving the neighborhood, and also to organize the houses into levels within the neighborhood.

The output shows that the neighborhood is connected, which means that Kim can visit all her neighbors without leaving the neighborhood. The output also provides a list of the houses in each level of the neighborhood. For example, house number 1 is in the first level, house numbers 2 and 3 are in the second level, and so on. This information can be helpful for Kim to easily remember which neighbors live in what part of the neighborhood.

# Problem 2: Ally's is training
**DFS Algorithm**

**Informal Description**: 
Ally is training in a new neighboorhood wants to explore. She wants to travel through every street. She is training for an upcoming race so she does not mind repeating streets. Ally is starting at house A and hopes to end at the closest spot. 

> **Formal Description**:
>  * Input: A graph of 20 nodes and 31 edges - edges labelled with realative street names and nodes labeled by letters.
>  * Output: (String) Path of houses to travel through every street in the neighborhood at least once.
**Setup code**:

```python
import networkx as nx
import matplotlib.pyplot as plt
```

**Visualization**:

![Allys's Neighborhood](/Ana_graph.png)

**Solution code:**
```python
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



```

**Output**  
These is the path:
('A', 'O'), ('O', 'I'), ('I', 'C'), ('C', 'N'), ('N', 'D'), ('D', 'E'), ('E', 'M'), ('M', 'R'), ('R', 'T'), ('T', 'B'), ('R', 'P'), ('P', 'L'), ('L', 'K'), ('K', 'J'), ('J', 'G'), ('G', 'H'), ('G', 'F'), ('I', 'S')

**Interpretation of Results**:
Depth first search is defined to traverse every node or "house". 
These results show a path for Ally to traverse through the entire neighboorhood without skipping any streets or houses. 