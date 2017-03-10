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





