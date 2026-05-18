from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS Function
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Menu Driven Program
while True:
    print("\n----- MENU -----")
    print("1. DFS Traversal")
    print("2. BFS Traversal")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        start = input("Enter starting node for DFS: ")
        print("DFS Traversal:")
        dfs(graph, start)
        print()

    elif choice == 2:
        start = input("Enter starting node for BFS: ")
        print("BFS Traversal:")
        bfs(graph, start)
        print()

    elif choice == 3:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")