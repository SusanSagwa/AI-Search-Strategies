import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(3, 7)
g.add_edge(7, 6)
g.add_edge(4, 8)
g.add_edge(8, 9)
g.add_edge(9, 6)
g.add_edge(4, 8)
g.add_edge(8, 10)
g.add_edge(10, 7)
g.add_edge(7, 6)
g.add_edge(5, 8)
g.add_edge(8, 9)
g.add_edge(9, 6)
g.add_edge(5, 8)
g.add_edge(8, 10)
g.add_edge(10, 7)
g.add_edge(7, 6)


nx.draw_spring(g, with_labels = True)
plt.savefig("filename.png")
