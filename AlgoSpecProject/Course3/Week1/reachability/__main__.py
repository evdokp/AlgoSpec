#Uses python3

import sys

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for node in set(graph[start]) - visited:
        dfs(graph, node, visited)
    return visited

def reach(adj, x, y):
    visited = dfs(adj, x)
    return 1 if y in visited else 0

if __name__ == '__main__':
    #input = sys.stdin.read()
    input = """4 3
1 2
3 2
4 3"""
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
