"""
Day 15
"""
from collections import namedtuple
from queue import PriorityQueue
import sys

Element = namedtuple('Element', 'element x y')


class Chiton:

    def __init__(self, risk_map):
        self.risk_map = [[int(element) for element in line] for line in risk_map]

    def __repr__(self):
        return '\n'.join(''.join(str(row)) for row in self.risk_map)

    def __str__(self):
        return '\n'.join(''.join(str(row)) for row in self.risk_map)

    def _get_element_2d(self, y, x):
        """
        Function to return the element if in range, else return None
        :param y: Vertical index
        :param x: Horizontal index
        :return: Element if in range else None
        """
        return Element(self.risk_map[y][x], x, y) if 0 <= y < len(self.risk_map) and 0 <= x < len(
            self.risk_map[0]) else None

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

    def five_times_as_large(self):
        width = len(self.risk_map[0])
        height = len(self.risk_map)
        for i in range(4):
            for line in self.risk_map:
                line.extend([x % 9 + 1 for x in line[-width:]])
            for line in self.risk_map[height * i:height * (i + 1)]:
                self.risk_map.append([x % 9 + 1 for x in line])
        return self

    def dijkstra_path(self):
        # queue = [self._get_element_2d(y, x) for y in range(len(self.risk_map)) for x in range(len(self.risk_map[y]))]
        queue = PriorityQueue()
        distance = {}
        previous = {}
        start, end = self._get_element_2d(0, 0), self._get_element_2d(len(self.risk_map) - 1, len(self.risk_map[0]) - 1)
        for y in range(len(self.risk_map)):
            for x in range(len(self.risk_map[y])):
                element = self._get_element_2d(y, x)
                distance[element] = sys.maxsize
                previous[element] = None
        distance[start] = 0
        queue.put((distance[start], start))
        while not queue.empty():
            u = queue.get()[1]
            neighbors = [neighbor for neighbor in self._get_adjacent_nodes_2d(u.y, u.x)]
            for v in neighbors:
                alt = distance[u] + v.element
                if v not in previous or alt < distance[v]:
                    distance[v] = alt
                    previous[v] = u
                    queue.put((distance[v], v))
        return distance[end]


def main():
    with open("input.txt", "r") as file:
        chiton = Chiton(list(file.read().splitlines()))
    print(chiton.dijkstra_path())  # Part 1
    chiton.five_times_as_large()
    print(chiton.dijkstra_path())  # Part 2


if __name__ == '__main__':
    main()
