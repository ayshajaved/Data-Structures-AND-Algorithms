class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        # For undirected graph, uncomment the next line
        # self.matrix[v][u] = weight

    def display(self):
        for row in self.matrix:
            print(row)

class GraphList:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.adj_list[u].append((v, weight))
        # For undirected graph, uncomment the next line
        # self.adj_list[v].append((u, weight))

    def display(self):
        for i in range(self.V):
            print(f"Vertex {i}: {self.adj_list[i]}")

def bfs(graph, start):
    visited = [False] * graph.V
    queue = []
    result = []
    
    queue.append(start)
    visited[start] = True
    
    while queue:
        vertex = queue.pop(0)
        result.append(vertex)
        
        for neighbor, _ in graph.adj_list[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    return result

def dfs(graph, start):
    visited = [False] * graph.V
    result = []
    
    def dfs_util(vertex):
        visited[vertex] = True
        result.append(vertex)
        
        for neighbor, _ in graph.adj_list[vertex]:
            if not visited[neighbor]:
                dfs_util(neighbor)
    
    dfs_util(start)
    return result

def topological_sort(graph):
    visited = [False] * graph.V
    stack = []
    
    def dfs_util(vertex):
        visited[vertex] = True
        
        for neighbor, _ in graph.adj_list[vertex]:
            if not visited[neighbor]:
                dfs_util(neighbor)
        
        stack.append(vertex)
    
    for i in range(graph.V):
        if not visited[i]:
            dfs_util(i)
    
    return stack[::-1]  # Reverse to get correct topological order

# Example usage
if __name__ == "__main__":
    # Adjacency Matrix Example
    print("Adjacency Matrix Representation:")
    g_matrix = GraphMatrix(4)
    g_matrix.add_edge(0, 1)
    g_matrix.add_edge(0, 2)
    g_matrix.add_edge(1, 2)
    g_matrix.add_edge(2, 0)
    g_matrix.add_edge(2, 3)
    g_matrix.add_edge(3, 3)
    g_matrix.display()

    # Adjacency List Example
    print("\nAdjacency List Representation:")
    g_list = GraphList(4)
    g_list.add_edge(0, 1)
    g_list.add_edge(0, 2)
    g_list.add_edge(1, 2)
    g_list.add_edge(2, 0)
    g_list.add_edge(2, 3)
    g_list.add_edge(3, 3)
    g_list.display()

    # BFS Example
    print("\nBFS Traversal starting from vertex 2:")
    bfs_result = bfs(g_list, 2)
    print(bfs_result)

    # DFS Example
    print("\nDFS Traversal starting from vertex 2:")
    dfs_result = dfs(g_list, 2)
    print(dfs_result)

    # Topological Sort Example
    print("\nTopological Sort:")
    g_topo = GraphList(6)
    g_topo.add_edge(5, 2)
    g_topo.add_edge(5, 0)
    g_topo.add_edge(4, 0)
    g_topo.add_edge(4, 1)
    g_topo.add_edge(2, 3)
    g_topo.add_edge(3, 1)
    topo_result = topological_sort(g_topo)
    print(topo_result)