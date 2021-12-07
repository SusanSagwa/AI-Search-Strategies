import networkx as nx
import matplotlib.pyplot as plt
import queue as Q
from collections import defaultdict
def gbfs(adjacencyList, heuristics):
    i = 0
    sVertex=max(heuristics,key=heuristics.get)
    print(sVertex)
    fVertex=min(heuristics,key=heuristics.get)
    print(fVertex)
    visitedSet = set()
    queue = []
    visitedSet.add(sVertex)
    queue.append(sVertex)
    result=[]
    while queue:
        search=[]
        v = queue[i]
        if v == fVertex:
            result.append(v)
            break
        result.append(v)
        for neighbor in adjacencyList[v]:
            if neighbor not in visitedSet:
                search.append(heuristics[neighbor])
        x = min(search,default="Nimededi")
        for k, v in heuristics.items():
            if x == v:
                queue.append(k)
                visitedSet.add(k)
        i+=1
    return result
def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList
edges = [["SportsComplex","Siwaka"]
         ,["Siwaka","Ph1.A"]
         ,["Ph1.A","Ph1.B"]
         ,["Siwaka","Ph1.B"]
         ,["Ph1.A","Mada"]
         ,["Ph1.B","Phase2"]
         ,["Ph1.B","STC"]
         ,["STC","Phase2"]
         ,["STC","ParkingLot"]
         ,["Phase2","J1"]
         ,["Phase2","Phase3"]
         ,["Phase3","ParkingLot"]
         ,["J1","Mada"]
         ,["Mada","ParkingLot"]]
adjacencyList = generateAdjacencyLst(edges)
for i in adjacencyList:
    print(i)
    print(adjacencyList[i])
heuristics = {
    'SportsComplex':730,
    'Siwaka':405,
    'Ph1.A':380,
    'Ph1.B':280,
    'STC':213,
    'Phase2':210,
    'J1':500,
    'Phase3':160,
    'Mada':630,
    'ParkingLot':0
    }
x = gbfs(adjacencyList,heuristics)
for i in x:
    print(x)
g = nx.Graph()
nodes = ["SportsComplex","Siwaka","Ph1.A","Ph1.B","Phase2","STC","J1",
         "Phase3","ParkingLot","Mada"]
g.add_nodes_from(nodes)
g.add_edges_from(edges)
node_sizes=300
pos_nodes = nx.spring_layout(g, seed=3113794652)
nx.draw(g,pos_nodes,with_labels=1,node_size=500)
nx.draw_networkx_nodes(g,pos_nodes,nodelist=nodes,node_size=node_sizes)
nx.draw_networkx_nodes(g,pos_nodes,nodelist=x,node_color="tab:red",node_size=node_sizes)
nx.draw_networkx_edge_labels(g,pos_nodes,edge_labels={
    ("SportsComplex","Siwaka"):"UnkRoad 450m"
    ,("Siwaka","Ph1.A"):"SangaleRd 10m"
    ,("Ph1.A","Ph1.B"):"ParkingWalkWay 100m"
    ,("Siwaka","Ph1.B"):"SangaleLink 230m"
    ,("Ph1.A","Mada"):"SangaleRd 850m"
    ,("Ph1.B","Phase2"):"KeriRd 112m"
    ,("Ph1.B","STC"):"KeriRd 50m"
    ,("STC","Phase2"):"STCwalkway 50m"
    ,("STC","ParkingLot"):"LibraryWalkWay 250m"
    ,("Phase2","J1"):"KeriRd 600m"
    ,("Phase2","Phase3"):"KeriRd 500m"
    ,("Phase3","ParkingLot"):"HimaGardensRd 350m"
    ,("J1","Mada"):"SangaleRd 200m"
    ,("Mada","ParkingLot"):"langataRd 700m"
    },font_size=7,horizontalalignment='center', verticalalignment='center')
plt.show()
