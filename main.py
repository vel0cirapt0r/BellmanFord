import os

from graph_parser import GraphParser
from decorators import measure_time
import filepaths


class BellmanFord:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.distances = {vertex: float('inf') for vertex in graph}
        self.distances[source] = 0

    @measure_time
    def run(self):
        num_vertices = len(self.graph)
        for _ in range(num_vertices - 1):
            for u in self.graph:
                for v, weight in self.graph[u].items():
                    self.relax(u, v, weight)

        self.check_negative_cycles()

    def relax(self, u, v, weight):
        if self.distances[u] + weight < self.distances[v]:
            self.distances[v] = self.distances[u] + weight

    def check_negative_cycles(self):
        for u in self.graph:
            for v, weight in self.graph[u].items():
                if self.distances[u] + weight < self.distances[v]:
                    raise ValueError("Graph contains a negative cycle")



if __name__ == "__main__":
    dataset_folder_path = input('Enter path to graph files folder: ') or filepaths.DATASET_PATH
    files_path = input('Enter name of graph files: ') or 'bay'
    folder_path = os.path.join(dataset_folder_path, files_path)
    parser = GraphParser()
    parsed_graph = parser.parse(folder_path)

    source = '34'  # Set the source node
    bellman_ford = BellmanFord(parsed_graph['distance_edges'], source)
    bellman_ford.run()
    print("Distances:", bellman_ford.distances)
