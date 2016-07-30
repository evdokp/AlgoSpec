#Uses python3

import sys

index = 0

def previsit(v, previsit_data):
    global index
    index += 1
    previsit_data[v] = index

def postvisit(v, postvisit_data):
    global index
    index += 1
    postvisit_data[v] = index

def explore(v, graph, visited,previsit_data, postvisit_data):
    visited[v] = True
    previsit(v, previsit_data)
    for w in graph[v]:
        if not visited[w]:
            explore(w, graph, visited, previsit_data, postvisit_data)
    postvisit(v, postvisit_data)

def dfs(adj, used, order, x):
    visited = [False for _ in adj]
    previsit_data = [0 for _ in adj]
    postvisit_data = [0 for _ in adj]
    for v in range(len(adj)):
        if not visited[v]:
            explore(v, adj, visited, previsit_data, postvisit_data)

    return postvisit_data

def toposort(adj):
    used = [0] * len(adj)
    order = []

    postorder = dfs(adj, used, order, 0)
    order = {i:item for i, item in enumerate(postorder)}
    sortdict = sorted(order, key=order.get)

    return list(reversed(sortdict))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

