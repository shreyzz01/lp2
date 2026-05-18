def dijkstra(graph, start):
    
    # Store shortest distances
    distance = {}

    # Set all distances to infinity
    for vertex in graph:
        distance[vertex] = float('inf')

    # Distance of starting node = 0
    distance[start] = 0

    visited = []

    # Repeat for all vertices
    while len(visited) < len(graph):

        min_node = None

        # Find unvisited node with minimum distance
        for node in graph:
            if node not in visited:
                if min_node is None or distance[node] < distance[min_node]:
                    min_node = node

        visited.append(min_node)

        # Update distances of neighbors
        for neighbor, weight in graph[min_node]:

            new_distance = distance[min_node] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

    return distance


# Graph with 5 vertices
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('E', 3)],
    'D': [('B', 7), ('E', 1)],
    'E': [('C', 3), ('D', 1)]
}

# Run algorithm from vertex A
result = dijkstra(graph, 'A')

print("Shortest distances from A:")

for node in result:
    print(node, "=", result[node])