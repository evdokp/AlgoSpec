# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)



class TreeHeight:
        def __init__(self):
            self.nodes = []
            self.root = None

        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.fill_tree()

        def load(self, n, parent):
                self.n = n
                self.parent = parent
                self.fill_tree()

        def fill_tree(self):

            for x in range(self.n):
                node = Node(x)
                self.nodes.append(node)

            for x in range(self.n):
                parent = self.parent[x]
                if parent < 0:
                    self.root = self.nodes[x];
                else:
                    self.nodes[parent].add_child(self.nodes[x])

            pass

        def compute_height(self):
            return self.compute_height_internal(self.root)

        def compute_height_internal(self, node):
            if node is None:
                return 0;
            else:
                allDepths = [self.compute_height_internal(x) for x in node.children]
                if len(allDepths) == 0:
                    return 1
                else:
                    return max(allDepths) + 1






def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
