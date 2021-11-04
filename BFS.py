#pseudo code
#function BREADTH-FIRST_SEARCH(problem) returns a solution. or failure
# node <- node with STATE = problem.INITIAL-STATE, PATH-COST=0
#if problem.GOL-TEST(node.STATE)then return SOLUTION(node)
#frontier <- a FIFO queue with node as the only element
#explored <- an empty set
#loop do
#if EMPTY?(frontier) /* chooses the shallowest node in fronteir */
#add node.STATE to explored
#for each action in problem.ACTIONS(node.STATE)do
#child <-CHILD-NODE(problem,node,action)
#if child.STATE is not in explored or frontier then 
#if problem.GOAL-TEST(child.STATE)then return SOLUTION(child)\
#frontier <- INSERT(child.frontier)





def breadth_first_graph_search(problem):
  
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None


def best_first_graph_search(problem, f, display=False):
    
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), len(frontier), )
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None