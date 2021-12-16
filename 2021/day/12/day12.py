"""
Day 12
"""
from collections import defaultdict
import json


class CaveSystem:
    def __init__(self, system):
        self.system = system
        self.graph = defaultdict(list)
        self._add_edges()

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

    def find_paths_part1(self, path=None, paths=None, visited=None, start='start', end='end'):
        if path is None:
            path = [start]
        if paths is None:
            paths = 0
        if visited is None:
            visited = {key: 0 for key in self.graph.keys()}
        for neighbor in self.graph[start]:
            if neighbor == 'start':
                continue
            elif neighbor == 'end':
                path.append(neighbor)
                paths += 1
                path.pop()
                continue
            else:
                path.append(neighbor)
                if visited[neighbor] <= 0:
                    if neighbor.islower():
                        visited[neighbor] += 1
                    paths = self.find_paths_part1(path, paths, visited, neighbor, end)
                    visited[neighbor] -= 1
                path.pop()
        return paths

    def find_paths_part2(self, path=None, paths=None, visited=None, start='start', end='end'):
        if path is None:
            path = [start]
        if paths is None:
            paths = 0
        if visited is None:
            visited = {key: 0 for key in self.graph.keys()}
        for neighbor in self.graph[start]:
            if neighbor == 'start':
                continue
            elif neighbor == 'end':
                path.append(neighbor)
                paths += 1
                path.pop()
                continue
            else:
                path.append(neighbor)
                if visited[neighbor] <= 1:
                    if neighbor.islower():
                        if visited[neighbor] != 1 or max(visited.values()) < 2:
                            visited[neighbor] += 1
                        else:
                            continue
                    paths = self.find_paths_part2(path, paths, visited, neighbor, end)
                    visited[neighbor] -= 1
                path.pop()
        return paths


def main():
    with open("input.txt", "r") as file:
        system = CaveSystem(list(file.read().splitlines()))
    print(system.find_paths_part1())  # Part 1
    print(system.find_paths_part2())  # Part 2


if __name__ == '__main__':
    main()
