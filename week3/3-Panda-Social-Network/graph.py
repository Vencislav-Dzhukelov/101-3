"""
1 <-> 2
1 <-> 3
2 <-> 4
4 <-> 5
5 <-> 1
6 <-> 4
3 <-> 6
6 <-> 7
7 <-> 8
9 <-> 8
10 <-> 9
1- <-> 1
"""

graph = {
    "1": ["2", "3", "5", "10"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9", "1"],
    "11": ["12"],
    "12": ["11"]
}


def bfs(graph, start, end):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            return True

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return False

print (bfs(graph, "1", "11"))
