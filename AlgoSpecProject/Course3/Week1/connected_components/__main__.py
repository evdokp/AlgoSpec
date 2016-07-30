#Uses python3

import sys

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for node in set(graph[start]) - visited:
        dfs(graph, node, visited)
    return visited


def number_of_components(adj):
    cc_count = 0
    remaining_nodes = set(range(0,len(adj)))
    while len(remaining_nodes) > 0:
        start_node = list(remaining_nodes)[0]
        cc = dfs(adj, start_node)
        remaining_nodes = remaining_nodes - cc
        cc_count += 1
    return cc_count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
