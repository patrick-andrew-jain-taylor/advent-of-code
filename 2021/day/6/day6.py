"""
Day 5
"""


class LanternSchool:
    """
    Implementation of a school of lanternfish.
    """

    def __init__(self, start):
        self.school = [LanternFish(age) for age in range(9)]
        for age in start.split(','):
            self.school[int(age)].add_fish(1)

    def __next__(self):
        # Track 0 count
        reset_count = self.school[0].count
        # All counts shift
        for i in range(1, len(self.school)):
            self.school[i - 1].count = self.school[i].count
        # Add new 8 to end of list
        self.school[8].count = reset_count
        # 0 becomes 6
        self.school[6].add_fish(reset_count)
        return self

    def __repr__(self):
        return ','.join(str(fish.count) for fish in self.school)

    def __str__(self):
        return ','.join(str(fish.count) for fish in self.school)

    def total(self):
        return sum(fish.count for fish in self.school)


class LanternFish:
    """
    Implementation of a lanternfish running on q cycle.
    """

    def __init__(self, age, count=0):
        self.age = age
        self.count = count

    def add_fish(self, count):
        self.count += count
        return self

    def __repr__(self):
        return str(self.age)

    def __str__(self):
        return str(self.age)


def main():
    with open("input.txt", "r") as file:
        ages = file.read().strip()
    fishes = LanternSchool(ages)
    for _ in range(256):
        next(fishes)
    print(fishes.total())


if __name__ == '__main__':
    main()
