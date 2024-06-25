import os

from graph_parser import GraphParser
from decorators import measure_time
from filepaths import DATASET_PATH
from sample_graph_generator import generate_graph


class BellmanFord:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.distances = {vertex: float('inf') for vertex in graph}
        self.distances[source] = 0

    @measure_time
    def run(self):
        # print(type(self.source))
        num_vertices = len(self.graph)
        for _ in range(num_vertices - 1):
            for u in self.graph:
                for v, weight in self.graph[u].items():
                    # print(type(u), type(v))
                    # print(v, weight, self.distances[u], self.distances[v])
                    if self.distances[u] + weight < self.distances[v]:
                        self.distances[v] = self.distances[u] + weight

        self.check_negative_cycles()

        return self.distances

    def check_negative_cycles(self):
        for u in self.graph:
            for v, weight in self.graph[u].items():
                if self.distances[u] + weight < self.distances[v]:
                    raise ValueError("Graph contains a negative cycle")


# if __name__ == "__main__":
#     # dataset_folder_path = input('Enter path to graph files folder: ') or DATASET_PATH
#     # files_path = input('Enter name of graph files: ') or 'bay'
#     # folder_path = os.path.join(dataset_folder_path, files_path)
#     #
#     # parser = GraphParser()
#     # parsed_graph = parser.parse(folder_path)
#     # graph = parsed_graph['distance_edges']
#     #
#     # total_edges = sum(len(adjacent_vertices) for adjacent_vertices in graph.values())
#     # print('number of nodes: ', len(graph), ', number of edges: ', total_edges)
#     # print(type(graph))
#
#     graph = generate_graph(32127, 79483)
#     # print("generated graph: ", graph)
#
#     source = int(input('Enter source for graph: ') or '1')  # Set the source node
#     bellman_ford = BellmanFord(graph, source)
#     bellman_ford.run()
#     print("Distances:", bellman_ford.distances)

if __name__ == "__main__":
    print("Bellman-Ford Algorithm Implementation\n")

    choice = input("Choose an option:\n"
                   "1. Generate a new graph\n"
                   "2. Use a prepared graph\n"
                   "Option: ")

    if choice == '1':
        num_nodes = int(input("Enter the number of nodes for the new graph: "))
        num_edges = int(input("Enter the number of edges for the new graph: "))
        graph = generate_graph(num_nodes, num_edges)
    elif choice == '2':
        dataset_folder_path = input("Enter path to graph files folder: ") or DATASET_PATH
        files_path = input("Enter name of graph files: ") or 'bay'
        folder_path = os.path.join(dataset_folder_path, files_path)

        parser = GraphParser()
        parsed_graph = parser.parse(folder_path)
        graph = parsed_graph['distance_edges']
    else:
        print("Invalid choice. Please choose '1' or '2'.")
        exit()

    source = int(input("Enter source for graph: ") or '1')  # Set the source node
    bellman_ford = BellmanFord(graph, source)
    distances = bellman_ford.run()
    print("Distances:", distances)
