

graph=[['S','A',450],
       ['A','B',10],
       ['A','C',230],
       ['B','C',100],
       ['C','D',50],
       ['C','E',112],
       ['E','F',600],
       ['F','G',200],
       ['B','G',850],
       ['E','D',50],
       ['E','H',500],
       ['D','I',250],
       ['H','I',350],
       ['G','I',700] ]


temp = []
temp1 = []
for i in graph:
  temp.append(i[0])
  temp1.append(i[1])
nodes = set(temp).union(set(temp1))
def UCS(graph, costs, open, closed, cur_node):
  if cur_node in open:
    open.remove(cur_node)
  closed.add(cur_node)
  for i in graph:
    if(i[0] == cur_node and costs[i[0]]+i[2] < costs[i[1]]):
      open.add(i[1])
      costs[i[1]] = costs[i[0]]+i[2]
      path[i[1]] = path[i[0]] + ' -> ' + i[1]
  costs[cur_node] = 999999
  small = min(costs, key=costs.get)
  if small not in closed:
      UCS(graph, costs, open,closed, small)
costs = dict()
temp_cost = dict()
path = dict()
for i in nodes:
  costs[i] = 999999
  path[i] = ' '
open = set()
closed = set()
start_node = input("Enter the Start State: ")
open.add(start_node)
path[start_node] = start_node
costs[start_node] = 0
UCS(graph, costs, open, closed, start_node)


goal_node = input("Enter the Goal State: ")
print("Path with least cost is: ",path[goal_node])