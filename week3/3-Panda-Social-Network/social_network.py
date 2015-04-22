from panda import Panda
import json


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.social_network = {}

    def add(self, panda):
        if panda not in self.social_network:
            self.social_network[panda] = []
        else:
            raise PandaAlreadyThere

    def has_panda(self, panda):
        return panda in self.social_network

    def get_social_network(self):
        return self.social_network

    def make_friends(self, panda1, panda2):
        if panda2 in self.social_network.keys() and \
                    panda1 in self.social_network[panda2]:
            raise PandasAlreadyFriends
        if panda1 in self.social_network.keys():
            self.social_network[panda1].append(panda2)
        else:
            self.social_network[panda1] = [panda2]
        if panda2 in self.social_network.keys():
            self.social_network[panda2].append(panda1)
        else:
            self.social_network[panda2] = [panda1]

    def are_friends(self, panda1, panda2):
        return panda2 in self.social_network[panda1]

    def friends_of(self, panda):
        if panda not in self.social_network.keys():
            return False
        else:
            return self.social_network[panda]

    def connection_level(self, panda1, panda2):
        if not (panda1 in self.social_network.keys() and
                panda2 in self.social_network.keys()):
            return False
        elif panda1 in self.social_network[panda2]:
            return 1

        graph = self.social_network
        visited = set()
        queue = []
        # path_to[x] = y
        # if we go to x through y
        path_to = {}

        queue.append(panda1)
        visited.add(panda1)
        path_to[panda1] = None
        found = False
        path_length = 0

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == panda2:
                found = True
                break

            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    path_to[neighbour] = current_node
                    visited.add(neighbour)
                    queue.append(neighbour)

        if found:
            while path_to[panda2] is not None:
                path_length += 1
                panda2 = path_to[panda2]

        return path_length

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != 0

    def how_many_gender_in_network(self, level, panda, gender):
        count = 0
        for other_panda in self.social_network.keys():
            if other_panda != panda and \
                    (self.connection_level(panda, other_panda) <= level and
                        other_panda.gender == gender):
                count += 1
        return count


def save_to(path, data):
    json_string = json.dumps(data, indent=4)

    with open(path, "w") as f:
        f.write(json_string)


def load_from(path):
    with open(path, "r") as f:
        contents = f.read()

    return json.loads(contents)


network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")

for panda in [ivo, rado, tony]:
    network.add(panda)

network.make_friends(ivo, rado)
network.make_friends(rado, tony)

# save_to("save_network.json", repr(network))
load_from("save_network.json")
