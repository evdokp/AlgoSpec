# python3
import sys

class Node:
    def __init__(self):
        self.key = ''
        pass

    def __hash__(self):
        return hash(self.key)


class DiGraph:
    def __init__(self):
        self.edges = {}
        self.nodes_data = {}

    def __getitem__(self, item):
        return self.nodes_data[item]


    def nodes(self):
        return self.edges.keys()

    def get_all_edges(self):
        return self.edges

    def get_edges(self, v):
        return self.edges[v]

    def get_edge_data(self, v, w):
        return self.edges[v][w]

    def get_outedges(self, key, filter_data_dict):
        result = []
        for x in self.edges[key]:
            for filter_key in filter_data_dict:
                if filter_key in self.edges[key][x].keys():
                    if self.edges[key][x][filter_key] == filter_data_dict[filter_key]:
                        result.append(x)
        return result

    def add_node(self, new_node_key, node_data):
        if new_node_key in self.edges.keys():
            raise ValueError("{} is already added".format(new_node_key))
        else:
            self.edges[new_node_key] = {}
            self.nodes_data[new_node_key] = node_data
            self.nodes_data[new_node_key]['o'] = 0
            self.nodes_data[new_node_key]['i'] = 0

    def add_edge(self, from_node, to_node, data_dict):
        if from_node not in self.edges.keys():
            self.edges[from_node] = {}
        self.edges[from_node][to_node] = data_dict
        self.nodes_data[from_node]['o'] += 1
        self.nodes_data[to_node]['i'] += 1

    def remove_edge(self, from_node, to_node):
        if to_node in self.edges[from_node]: del self.edges[from_node][to_node]
        self.nodes_data[from_node]['o'] -= 1
        self.nodes_data[to_node]['i'] -= 1

    def remove_node(self, v):
        if v in self.edges: del self.edges[v]
        if v in self.nodes_data: del self.nodes_data[v]



    def in_degree(self, v):
        return self.nodes_data[v]['i']

    def out_degree(self, v):
        return self.nodes_data[v]['o']


class SuffixTrie:
    def __init__(self, text):
        # initialize and add root
        self.ROOT = 0
        self.DOLLARCHAR = '$'
        self.trie = DiGraph()
        self.trie.add_node(self.ROOT, {})
        self.edges_ext = dict()
        self.nodes_count = 1
        self.__construct(text)

    def __add_node(self, symbol, startpos):
        new_key = self.nodes_count + 1
        node_data = {}
        if symbol == self.DOLLARCHAR:
            node_data['s'] = startpos
        self.nodes_count += 1
        self.trie.add_node(new_key, node_data)

        return new_key

    def __add_edge(self, v, u, symbol, position, startpos):
        edge_data = {
            'x': symbol,
            'p': position
        }
        if symbol == self.DOLLARCHAR:
            edge_data['s'] = startpos

        self.trie.add_edge(v, u, edge_data)

    def __construct(self, text):
        for i in range(len(text)):
            cur_node = self.ROOT
            for j in range(i, len(text)):
                cur_symbol = text[j]

                match_edges = self.trie.get_outedges(cur_node,{'x': cur_symbol})

                if len(match_edges) > 0:
                    cur_node = match_edges[0]
                else:
                    new_node = self.__add_node(cur_symbol, i)
                    self.__add_edge(cur_node, new_node, cur_symbol, j, i)
                    cur_node = new_node

    def get_graph(self):
        return self.trie


class SuffixTree:
    def __init__(self, text):
        self.suffix_trie = SuffixTrie(text)
        self.graph = self.suffix_trie.get_graph()
        self.__construct()

    def __construct(self):
        paths = [x for x in maximal_non_branching_paths(self.suffix_trie.get_graph()) if len(x) > 2]
        counter = 0
        for path in paths:
            self.__compress_path(path)
            counter+=1

    def __compress_path(self, path):
        first_node = path[0]
        last_node = path[-1]
        position = self.graph.get_edge_data(path[0], path[1])['p']
        length = len(path)-1
        combined_symbol = []
        for i in range(1, len(path)):
            edge_symbol = self.graph.get_edge_data(path[i-1], path[i])['x']
            combined_symbol.append(edge_symbol)
            self.graph.remove_edge(path[i-1], path[i])
        for i in range(1, len(path)-1):
            self.graph.remove_node(path[i])
        self.graph.add_edge(first_node, last_node, {
            'x': "".join(combined_symbol),
            'p': position,
            'length': length
        })

    def get_edges_labels(self):
        labels = []
        edge_data = self.graph.get_all_edges()
        for node in edge_data:
            for outedge in edge_data[node]:
                labels.append(edge_data[node][outedge]['x'])
        return labels

    def get_graph(self):
        return self.graph


def is_node_one_one(graph, node):
    inputs_count = graph.in_degree(node)
    outputs_count = graph.out_degree(node)
    return inputs_count == 1 and outputs_count == 1

def maximal_non_branching_paths(graph):
    paths = []
    used_nodes = []
    for v in graph.nodes():
        if not is_node_one_one(graph, v):
            if graph.out_degree(v) > 0:  # outputs count > 0
                vedges = graph.get_edges(v).keys()
                for e in vedges:
                    path = [v, e]  # add first two items
                    w = e
                    used_nodes.append(w)
                    while is_node_one_one(graph, w):
                        next_edge = [x for x in graph.get_edges(w).keys()][0]
                        path.append(next_edge)
                        w = next_edge
                        used_nodes.append(w)
                    paths.append(path)

    return paths


def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  st = SuffixTree(text)
  result = st.get_edges_labels()
  # Implement this function yourself
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))