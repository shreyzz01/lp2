def prims(graph,start):
    visited=[start]
    min_cost=0
    edges=[]

    while len(visited) < len(graph):
        min_edge=None

        for v in visited:
            for neighbor,weight in graph[v]:
                if neighbor not  in visited:
                    if min_edge is None or weight<min_edge[2]:
                        min_edge=(v,neighbor,weight)
        
        visited.append(min_edge[1])
        edges.append(min_edge)
        min_cost +=min_edge[2]
    
    return edges,min_cost

graph = {
    'A': [('B', 4), ('C', 6)],
    'B': [('A', 4), ('C', 5), ('D', 2)],
    'C': [('A', 6), ('B', 5), ('D', 1)],
    'D': [('B', 2), ('C', 1)]
}

mst_edges, total_cost = prims(graph, 'A')

print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)

print("Total Cost:", total_cost)

'''
4 6
5,2
1
Concept of Prim’s Algorithm

Prim’s Algorithm is a Greedy Algorithm used to find the:

Minimum Spanning Tree (MST)

of a weighted graph.

A Minimum Spanning Tree is:

A tree connecting all vertices
Has no cycles
Has minimum possible total edge cost

edges = (start,end,weight)
'''