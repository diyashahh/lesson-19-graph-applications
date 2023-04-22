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
