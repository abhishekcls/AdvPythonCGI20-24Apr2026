from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            queue.extend(graph[node])


# Test
print("BFS")
bfs(graph, "A")

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node,end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


# Test
print("\nDFS")
dfs(graph, "A")