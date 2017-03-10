from Course4.Week1.suffix_tree.suffix_tree import SuffixTree

s2 = "aasdasd$"

st = SuffixTree(s2)

for x in st.get_edges_labels():
    print("".join(x))