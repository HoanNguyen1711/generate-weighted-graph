import osmnx as ox
import networkx as nx
import yaml


def load_areas():
    with open('areas_list.yaml') as f:
        areas = yaml.load(f, Loader=yaml.FullLoader)
    return areas


ox.config(log_console=True, use_cache=True)
place_name = load_areas()['areas']
src_node = load_areas()['src_node']
dest_node = load_areas()['dest_node']

combined_graph = None
for place in place_name:
    graph = ox.graph_from_place(place, network_type='drive')
    if combined_graph is None:
        combined_graph = graph
    else:
        combined_graph = nx.compose(combined_graph, graph)

graph_projected = ox.project_graph(combined_graph)

# Create a list of colors for all nodes, where the specified nodes have different colors
node_colors = ['red' if node == src_node or node == dest_node else 'white' for node in graph_projected.nodes]
node_sizes = [100 if node == src_node or node == dest_node else 8 for node in graph_projected.nodes]

# plot the network, also saving as image
fig, ax = ox.plot_graph(graph_projected, node_color=node_colors, node_size=node_sizes, save=True,
                        show=False, close=True, dpi=300, figsize=(20, 20))

# save graph to csv
nodes, edges = ox.graph_to_gdfs(graph_projected)
nodes.to_csv("nodes_origin.csv")
edges.to_csv("edges_origin.csv")

# remove unnecessary data
nodes = nodes[['street_count']]
edges = edges[['length', 'name']]
nodes.to_csv("nodes_processed.csv")
edges.to_csv("edges_processed.csv")

