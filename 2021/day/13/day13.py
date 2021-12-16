"""
Day 13
"""
from collections import namedtuple, Counter

Coordinate = namedtuple('Coordinate', 'x y')
Fold = namedtuple('Fold', 'direction position')


class ThermalCamera:

    def __init__(self, manual):
        index = manual.index('')
        self.coordinates = [Coordinate(*(coordinate.split(','))) for coordinate in manual[:index]]
        self.folds = [Fold(*(fold.split(' ')[2].split('='))) for fold in manual[index + 1:]]
        self.paper = [
            ['.' for _ in range(max(int(fold.position) for fold in self.folds if fold.direction == 'x') * 2 + 1)]
            for _ in range(max(int(fold.position) for fold in self.folds if fold.direction == 'y') * 2 + 1)
        ]
        self._add_dots_to_paper()

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.paper)

    def _add_dots_to_paper(self):
        for coordinate in self.coordinates:
            self.paper[int(coordinate.y)][int(coordinate.x)] = '#'
        return self

    def fold_paper(self, times=None):
        paper = [list()]
        if times is None:
            times = len(self.folds)
        for _ in range(times):
            fold = self.folds[0]
            position = int(fold.position)
            if fold.direction == 'x':
                paper = [
                    ['.' for _ in range(position)]
                    for _ in range(len(self.paper))
                ]
                for y in range(len(self.paper)):
                    for i, j in zip(range(position), range(len(self.paper[0]) - 1, position, -1)):
                        paper[y][i] = '#' if self.paper[y][i] == '#' or self.paper[y][j] == '#' else '.'
            elif fold.direction == 'y':
                paper = [
                    ['.' for _ in range(len(self.paper[0]))]
                    for _ in range(position)
                ]
                for i, j in zip(range(position), range(len(self.paper) - 1, position, -1)):
                    for x in range(len(self.paper[0])):
                        paper[i][x] = '#' if self.paper[i][x] == '#' or self.paper[j][x] == '#' else '.'
            self.folds.pop(0)
            self.paper = paper
        return self

    def count_dots(self):
        return Counter([position for row in self.paper for position in row]).get('#')


def main():
    with open("input.txt", "r") as file:
        thermal_camera = ThermalCamera(list(file.read().splitlines()))
    print(thermal_camera.fold_paper(1).count_dots())  # Part 1
    print(thermal_camera.fold_paper())  # Part 2


if __name__ == '__main__':
    main()
