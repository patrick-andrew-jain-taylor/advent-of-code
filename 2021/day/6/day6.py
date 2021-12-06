"""
Day 5
"""

from itertools import cycle, chain


class LanternSchool:
    """
    Implementation of a school of lanternfish.
    """

    def __init__(self, start):
        self.school = [LanternFish(age) for age in start.split(',')]

    def new_fish(self, fish):
        next(fish)
        if fish.age == 6 and fish.prev == 0:
            self.school.append(LanternFish())

    def __next__(self):
        for fish in self.school:
            self.new_fish(fish)
        return self

    def __repr__(self):
        return ','.join(str(fish) for fish in self.school)

    def __str__(self):
        return ','.join(str(fish) for fish in self.school)

    def total(self):
        return len(self.school)


class LanternFish:
    """
    Implementation of a lanternfish running on q cycle.
    """

    def __init__(self, age=8):
        self.age = age
        self.timer = chain(
            list(range(int(age), -1, -1)), cycle(list(range(6, -1, -1)))
        )

    def __next__(self):
        self.prev = self.age
        self.age = next(self.timer)
        return self

    def __repr__(self):
        return str(self.age)

    def __str__(self):
        return str(self.age)


def main():
    with open("input.txt", "r") as file:
        ages = file.read().strip()
    fishes = LanternSchool(ages)
    for _ in range(81):
        next(fishes)
    print(fishes.total())


if __name__ == '__main__':
    main()
