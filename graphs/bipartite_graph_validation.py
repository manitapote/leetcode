from typing import List
def bipartite_graph_validation(graph: List[List[int]]):
    colors = [0]*len(graph)
    for i in range(len(graph)):
        if colors[i] == 0 and dfs(i, graph, 1, colors) == False:
            return False
    return True


def dfs(node, graph, color, colors):
    colors[node] = color

    for neighbors in graph[node]:
        print(neighbors)
        if colors[neighbors] == color:
            return False

        if colors[neighbors] == 0 and dfs(neighbors, graph, -color, colors) == False:
            return False

    return True

graph = [[1, 4], [0, 2], [1], [4], [0, 3]]
print(bipartite_graph_validation(graph))
