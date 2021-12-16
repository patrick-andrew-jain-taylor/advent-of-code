"""
Day 12
"""
from collections import defaultdict
import json
import copy


class CaveSystem:
    def __init__(self, system):
        self.system = system
        self.graph = defaultdict(list)
        self._add_edges()
        self.paths = []

    def __repr__(self):
        return json.dumps(self.graph)

    def __str__(self):
        return json.dumps(self.graph)

    def _add_edge(self, u, v):
        self.graph[u].append(v)

    def _add_edges(self):
        for connection in self.system:
            self._add_edge(*connection.split('-'))
            self._add_edge(*reversed(connection.split('-')))

    def find_paths(self, path=None, visited=None, start='start', end='end'):
        if path is None:
            path = [start]
        if visited is None:
            visited = [start]
        for neighbor in self.graph[start]:
            if neighbor == 'start':
                continue
            elif neighbor == 'end':
                path.append(neighbor)
                self.paths.append(copy.copy(path))
                path.pop()
                continue
            else:
                path.append(neighbor)
                if neighbor not in visited:
                    if neighbor.islower():
                        visited.append(neighbor)
                    self.find_paths(path, visited, neighbor, end)
                    if neighbor == visited[-1]:
                        visited.pop()
                path.pop()
        return self.paths


def main():
    with open("input.txt", "r") as file:
        system = CaveSystem([line for line in file.read().splitlines()])
    paths = system.find_paths()
    print(len(paths))  # Part 1


if __name__ == '__main__':
    main()
