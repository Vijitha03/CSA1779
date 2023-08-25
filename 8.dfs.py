print("VIJITHA, 192124187")
print("depth first search")
from collections import defaultdict
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = defaultdict(list)
    graph[0] = [4, 2]
    graph[1] = [2]
    graph[2] = [0,4]
    graph[3] = [6]


    print("\nDFS traversal:")
    dfs(graph, 2)
