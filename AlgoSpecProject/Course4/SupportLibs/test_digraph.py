from Course4.SupportLibs.DiGraph import DiGraph

dg = DiGraph()
dg.add_node('k0')
dg.add_node('k1')
dg.add_node('k2')
dg.add_node('k3')
dg.add_edge('k0', 'k1', {'letter': 'a'})
dg.add_edge('k0', 'k2', {'letter': 'b'})
dg.add_edge('k0', 'k3', {})

filtered = dg.get_outedges('k0',{'letter': 'a'})
print(dg.edges)
print(filtered)

