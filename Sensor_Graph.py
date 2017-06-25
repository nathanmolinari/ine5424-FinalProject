import networkx as network
from Math_Utils import Math_Utils as math

class Sensor_Graph:

    graph = network.Graph()

    def contains(self, sensor):
        return sensor in self.graph

    def add_sensor(self, sensor):
        self.graph.add_node(sensor)

    def add_edges(self, sensor, list_of_reachable_sensor):
        for s in list_of_reachable_sensor:
            distance = math.get_distance_into(sensor, s)
            self.graph.add_edge(sensor, s, distance=distance)

    def len(self):
        return len(self.graph)

    def shortest_path(self, source, target):
        return list(network.dijkstra_path(self.graph, source, target, weight='distance'))
