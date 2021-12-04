"""
Day 2
"""


class Submarine:
    """Tracks certain components of the submarine.

    To use:
    >>> sub = Submarine(0, 0, 0)
    >>> sub.horz_pos
    0
    >>> sub.depth
    0

    Attributes:
        horz_pos: Horizontal Position of the Sub
        depth: Depth of the Sub
    """

    def __init__(self, horz_pos: int, depth: int, aim: int):
        """Inits Submarine with initial horizontal position & depth"""
        self.horz_pos = horz_pos
        self.depth = depth
        self.aim = aim
        self.action = {
            'down': self.__down,
            'forward': self.__forward,
            'up': self.__up
        }

    def __repr__(self):
        """Print representation of submarine"""
        return f"Submarine({self.horz_pos},{self.depth})"

    def __str__(self):
        """Print representation of submarine"""
        return f"{self.horz_pos * self.depth}"

    def move(self, moves):
        """Move submarine based on input"""
        direction, unit, *_ = moves.split()
        self.action[direction](int(unit))

    def __forward(self, unit):
        """Moves submarine forward"""
        # Part 1
        self.horz_pos += unit
        # Part 2
        self.depth += self.aim * unit

    def __up(self, unit):
        """Moves submarine up"""
        # Part 1
        # self.depth -= unit
        # Part 2
        self.aim -= unit

    def __down(self, unit):
        """Moves submarine down"""
        # Part 1
        # self.depth += unit
        # Part 2
        self.aim += unit


def main():
    submarine = Submarine(0, 0, 0)
    with open("input.txt", "r") as file:
        moves = list(file.read().splitlines())
    for move in moves:
        submarine.move(move)
    print(repr(submarine), submarine)


if __name__ == '__main__':
    main()
