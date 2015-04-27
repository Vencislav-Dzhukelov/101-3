class EdgeAlreadyThere(Exception):
    pass


class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, node_a, node_b):
        if node_a in self.graph.keys() and node_b in self.graph[node_a]:
            raise EdgeAlreadyThere
        if node_a in self.graph.keys():
            self.graph[node_a].append(node_b)
            self.graph[node_b] = []
        else:
            self.graph[node_a] = [node_b]
            self.graph[node_b] = []

    def get_neighbors_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        visited = set()
        queue = []

        queue.append(node_a)
        visited.add(node_a)

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == node_b:
                return True

            for neighbour in self.graph[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False

    def build_network(start, level):
        visited = set()
        queue = []
        graph = DirectedGraph()
        visited.add(start)
        queue.append((0, start))

        while len(queue) != 0:
            current_level, current_node = q.pop(0)
            if current_level > level:
                break

            network = get_network_for(current_node)

            for follower in network["followers"]:
                if follower not in visited:
                    queue.add_edge(follower , current_node)
                    visited.add(follower)
                    queue.append((current_level + 1, follower))
            queue.add_edge(current_node, following)
"""
graph1 = DirectedGraph()
graph1.add_edge("first", "second")
print (graph1.graph)
graph1.add_edge("first", "third")
print (graph1.graph)
print (graph1.get_neighbors_for("first"))
print (graph1.path_between("first", "second"))
print (graph1.path_between("first", "third"))
"""
