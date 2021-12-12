"""
Day 11
"""
from collections import namedtuple

Element = namedtuple('Element', 'element x y')


def get_element_2d(matrix_2d, y, x):
    """
    Function to return the element if in range, else return None
    :param matrix_2d: 2D matrix
    :param y: Vertical index
    :param x: Horizontal index
    :return: Element if in range else None
    """
    return Element(matrix_2d[y][x], x, y) if 0 <= y < len(matrix_2d) and 0 <= x < len(matrix_2d[0]) else None


def get_adjacent_nodes_2d(matrix_2d, y, x):
    """
    Function to retrieve adjacent nodes for a given element at positions (x, y)
    :param matrix_2d: 2D matrix
    :param y: Vertical index
    :param x: Horizontal index
    :return: Dictionary of elements
    """
    elements = {
        'up': get_element_2d(matrix_2d, y - 1, x),
        'up_right': get_element_2d(matrix_2d, y - 1, x + 1),
        'right': get_element_2d(matrix_2d, y, x + 1),
        'down_right': get_element_2d(matrix_2d, y + 1, x + 1),
        'down': get_element_2d(matrix_2d, y + 1, x),
        'down_left': get_element_2d(matrix_2d, y + 1, x - 1),
        'left': get_element_2d(matrix_2d, y, x - 1),
        'up_left': get_element_2d(matrix_2d, y - 1, x - 1)
    }
    return [element for element in elements.values() if element]


def flash(matrix_2d, y, x):
    matrix_2d[y][x] = 0
    for neighbor in get_adjacent_nodes_2d(matrix_2d, y, x):
        matrix_2d[neighbor.y][neighbor.x] += 1 if matrix_2d[neighbor.y][neighbor.x] else 0
        if matrix_2d[neighbor.y][neighbor.x] > 9:
            flash(matrix_2d, neighbor.y, neighbor.x)


def check_flash(matrix_2d):
    for y in range(len(matrix_2d)):
        for x in range(len(matrix_2d[0])):
            matrix_2d[y][x] += 1
    for y in range(len(matrix_2d)):
        for x in range(len(matrix_2d[0])):
            if matrix_2d[y][x] > 9:
                flash(matrix_2d, y, x)
    return sum(element.count(0) for element in matrix_2d)


def main():
    with open("input.txt", "r") as file:
        octopodes = [[int(digit) for digit in line] for line in file.read().splitlines()]
    print(sum(check_flash(octopodes) for _ in range(100)))


if __name__ == '__main__':
    main()
