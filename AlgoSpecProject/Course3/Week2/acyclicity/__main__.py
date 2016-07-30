#Uses python3

import sys

def explore(v, graph, visited, origin):
    visited[v] = True
    result = False
    for w in graph[v]:
        if w == origin:
            result = True
            if result:
                return result
        if not visited[w]:
            result = explore(w, graph, visited, origin)
            if result:
                break
    return result

def dfs(graph, start):
    visited = [False for _ in graph]
    for v in range(len(graph)):
        if not visited[v]:
            cyclic = explore(v, graph, visited, v)
            if cyclic:
                break
    return cyclic

def acyclic(adj):
    cyclic = dfs(adj, 0)
    return 1 if cyclic else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
