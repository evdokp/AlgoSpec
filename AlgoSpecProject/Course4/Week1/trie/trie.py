#Uses python3
import sys

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
        self.DOLLARNODEOFFSET = 10000
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

            out_edges_with_match = [x for x in self.trie.edges(v, data=True) if x[2]['letter'] == symbol]
            if len(out_edges_with_match) > 0:
                pattern.append(symbol)

                i += 1
                if i == len(text):
                    # check if current is final node
                    if self.__is_leaf(i):
                        return "".join(pattern)
                    else:
                        #print("No matches found. End of string.")
                        return


                else:
                    # move on
                    symbol = text[i]
                    edge = out_edges_with_match[0]
                    v = edge[1]
            else:
                #print("No matches found")
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


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = Trie(patterns).produce_output_dict()
    # write your code here
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
