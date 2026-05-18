def kruskal(nodes, edges):
    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])
    parent = {}
    # Initially every node is its own parent
    for node in nodes:
        parent[node] = node
    # Function to find parent
    def find(node):
        while parent[node] != node:
            node = parent[node]
        return node
    mst = []
    total_cost = 0
    # Check every edge
    for u, v, weight in edges:
        parent_u = find(u)
        parent_v = find(v)
        # If no cycle
        if parent_u != parent_v:
            # Add edge to MST
            mst.append((u, v, weight))
            # Add cost
            total_cost += weight
            # Union
            parent[parent_u] = parent_v
    return mst, total_cost

nodes = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 5),
    ('A', 'E', 4),
    ('E', 'D', 3),
    ('D', 'C', 2),
    ('B', 'C', 1),
    ('A', 'C', 1)
]
mst, cost = kruskal(nodes, edges)
print("MST:", mst)
print("Cost:", cost)


'''Concept of Kruskal’s Algorithm

Minimum Spanning Tree (MST)

Kruskal’s Algorithm is used to find the Minimum Spanning Tree (MST) of a graph.

What is MST?

A Minimum Spanning Tree is:

A set of edges that connects all vertices
Has no cycles
Has the minimum total weight
Main Idea of Kruskal’s Algorithm
Sort all edges by weight (smallest first)
Pick the smallest edge
Add it only if it does not form a cycle
Repeat until all nodes are connected
'''