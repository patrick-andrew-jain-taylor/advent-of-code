"""
Day 5
"""


class OceanFloor:
    """
    Representation of the ocean floor with geothermic vents.
    """

    def __init__(self, size: int):
        self.floor = [['.' for i in range(size)] for j in range(size)]

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.floor)

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.floor)

    def __diag_line(self, left, right):
        """
        Take action on the diagonal.
        :return:
        """
        horz_range = (
            range(int(left[0]), int(right[0]) + 1)
            if int(left[0]) < int(right[0])
            else range(int(left[0]), int(right[0]) - 1, -1)
        )
        vert_range = (
            range(int(left[1]), int(right[1]) + 1)
            if int(left[1]) < int(right[1])
            else range(int(left[1]), int(right[1]) - 1, -1)
        )
        for i, j in zip(horz_range, vert_range):
            self.floor[j][i] = '1' if self.floor[j][i] == '.' else f'{int(self.floor[j][i]) + 1}'
        return self.floor

    def __horz_line(self, left, right):
        """
        Take action on the horizontal.
        :return:
        """
        row = int(left[1])
        start, stop = min(int(left[0]), int(right[0])), max(int(left[0]), int(right[0]))
        for i in range(start, stop + 1):
            self.floor[row][i] = '1' if self.floor[row][i] == '.' else f'{int(self.floor[row][i]) + 1}'
        return self.floor

    def __vert_line(self, left, right):
        """
        Take action on the vertical.
        :return:
        """
        column = int(left[0])
        start, stop = min(int(left[1]), int(right[1])), max(int(left[1]), int(right[1]))
        for i in range(start, stop + 1):
            self.floor[i][column] = '1' if self.floor[i][column] == '.' else f'{int(self.floor[i][column]) + 1}'
        return self.floor

    def add_line(self, line):
        """
        Take in line segment, update floor
        :return:
        """
        left, right = line.split(' -> ')
        left, right = left.split(','), right.split(',')
        if left[0] == right[0]:
            self.__vert_line(left, right)
        elif left[1] == right[1]:
            self.__horz_line(left, right)
        else:
            self.__diag_line(left, right)

    def danger(self):
        """
        Determine number of danger points
        :return:
        """
        danger = 0
        for row in self.floor:
            for column in row:
                if column != '.' and int(column) >= 2:
                    danger += 1
        return danger


def main():
    with open("input.txt", "r") as file:
        lines = list(file.read().splitlines())
    floor = OceanFloor(1000)
    for line in lines:
        floor.add_line(line)
    print(floor.danger())


if __name__ == '__main__':
    main()
