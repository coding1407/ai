#bfs

graph = {
    'A':['B','E','C'],
    'B':['A','D','E'],
    'D':['B','E'],
    'E':['A','D','B'],
    'C':['A','F','G'],
    'F':['C'],
    'G':['C']
}

visited = []
stack = []

def dfs(graph,start_node,goal_node):
    print("DFS traversal is :")
    stack.append(start_node)
    visited.append(start_node)
    
    while stack:
        node = stack[-1]
        stack.pop()
        print("Node : ", node)
        
        if node == goal_node:
            print("Goal_Node is found !!")
            return
        
        for n in graph[node]:
            if n not in visited:
                    visited.append(n)
                    stack.append(n)

dfs(graph,'A','D')
