"""
Day 15
"""
from collections import namedtuple
import sys

Element = namedtuple('Element', 'element x y')


class Chiton:

    def __init__(self, map):
        self.map = [[int(element) for element in line] for line in map]

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.map)

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.map)

    def _get_element_2d(self, y, x):
        """
        Function to return the element if in range, else return None
        :param y: Vertical index
        :param x: Horizontal index
        :return: Element if in range else None
        """
        return Element(self.map[y][x], x, y) if 0 <= y < len(self.map) and 0 <= x < len(self.map[0]) else None

    def _get_adjacent_nodes_2d(self, y, x):
        """
        Function to retrieve adjacent nodes for a given element at positions (x, y)
        :param y: Vertical index
        :param x: Horizontal index
        :return: List of elements
        """
        elements = {
            'up': self._get_element_2d(y - 1, x),
            # 'up_right': self._get_element_2d(y - 1, x + 1),
            'right': self._get_element_2d(y, x + 1),
            # 'down_right': self._get_element_2d(y + 1, x + 1),
            'down': self._get_element_2d(y + 1, x),
            # 'down_left': self._get_element_2d(y + 1, x - 1),
            'left': self._get_element_2d(y, x - 1),
            # 'up_left': self._get_element_2d(y - 1, x - 1)
        }
        return [element for element in elements.values() if element]

    def dijkstra_path(self):
        queue = [self._get_element_2d(y, x) for y in range(len(self.map)) for x in range(len(self.map[y]))]
        distance = {self._get_element_2d(y, x): sys.maxsize for y in range(len(self.map)) for x in
                    range(len(self.map[y]))}
        previous = {self._get_element_2d(y, x): None for y in range(len(self.map)) for x in range(len(self.map[y]))}
        start, end = self._get_element_2d(0, 0), self._get_element_2d(len(self.map) - 1, len(self.map[0]) - 1)
        distance[start] = 0
        while queue:
            min_distance = min(distance[element] for element in queue)
            u = next(element for element in queue if distance[element] == min_distance)
            queue.pop(queue.index(u))
            neighbors = [neighbor for neighbor in self._get_adjacent_nodes_2d(u.y, u.x) if neighbor in queue]
            for v in neighbors:
                alt = distance[u] + v.element
                if alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u
        return distance[end]


def main():
    with open("input.txt", "r") as file:
        chiton = Chiton(list(file.read().splitlines()))
    print(chiton.dijkstra_path())


if __name__ == '__main__':
    main()
