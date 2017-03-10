# python3
import sys

NA = -1
class DiGraph:
    def __init__(self):
        self.edges = {}

    def get_edges(self):
        return self.edges

    def get_outedges(self, key, filter_data_dict):
        result = []
        for x in self.edges[key]:
            for filter_key in filter_data_dict:
                if filter_key in self.edges[key][x].keys():
                    if self.edges[key][x][filter_key] == filter_data_dict[filter_key]:
                        result.append(x)
        return result




    def add_node(self, new_node):
        if new_node in self.edges.keys():
            raise ValueError("{} is already added".format(new_node))
        else:
            self.edges[new_node] = {}

    def add_edge(self, from_node, to_node, data_dict):
        self.edges[from_node][to_node] = data_dict

class Trie:

    def __init__(self, words=[]):
        self.ROOT = 0
        self.DOLLARNODEOFFSET = 11000
        self.DOLLARCHAR = '$'
        self.real_nodes_count = 1
        self.dollar_nodes_count = 0
        self.trie = DiGraph()
        self.trie.add_node(self.ROOT)
        if len(words) > 0:
            count = 0
            for word in words:
                count += 1
                self.insert(word)

    def __add_node(self, letter):
        if letter == self.DOLLARCHAR:
            new_node_key = self.DOLLARNODEOFFSET + self.dollar_nodes_count
            self.dollar_nodes_count += 1
        else:
            new_node_key = self.real_nodes_count
            self.real_nodes_count += 1
        self.trie.add_node(new_node_key)
        return new_node_key

    def __is_leaf(self, v):
        leafs = self.trie.get_outedges(v, {'letter':self.DOLLARCHAR})
        return len(leafs) == 1

    def insert(self, input_word):
        word = input_word + '$'
        cur_node = self.ROOT
        for i in range(len(word)):
            out_edges = self.trie.get_outedges(cur_node, {'letter': word[i]})

            if len(out_edges) > 0:
                cur_node = out_edges[0]
            else:
                new_node_key = self.__add_node(word[i])
                self.trie.add_edge(cur_node, new_node_key, {'letter':word[i]})
                cur_node = new_node_key

    def is_prefix_in_trie(self, text):
        i = 0
        symbol = text[i]
        v = self.ROOT
        pattern = []
        while True:
            if self.__is_leaf(v):
                return "".join(pattern)
            if symbol == None:
                return

            out_edges_with_match = self.trie.get_outedges(v, {'letter': symbol})

            if len(out_edges_with_match) > 0:
                i += 1
                # we shifted, but the text ended!
                if len(text) == i:
                    symbol = None
                else:
                    symbol = text[i]
                v = out_edges_with_match[0]
            else:
                # print("No matches found")
                return

    def produce_output_dict(self):
        e = self.trie.get_edges()
        s = {}
        for x in e:
            for y in e[x]:
                if 'letter' in e[x][y]:
                    if e[x][y]['letter'] != '$':
                        if x not in s:
                            s[x] = {}
                        s[x][e[x][y]['letter']] = y
        return s




class Node:
    def __init__(self):
        self.next = [NA] * 4


def solve(text, n, patterns):
    indices = []
    trie = Trie(patterns)
    for start in range(len(text)):
            if trie.is_prefix_in_trie(text[start:]) != None:
                indices.append(start)
    return sorted(list(set(indices)))


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
