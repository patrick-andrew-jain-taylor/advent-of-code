"""
Day 14
"""
from collections import Counter


class Polymer:
    def __init__(self, formula):
        self.template = formula[0]
        self.insertion = {k: v for rule in formula[2:] for k, v in dict([rule.split(' -> ')]).items()}
        print(self.insertion)

    def __repr__(self):
        return self.template

    def __str__(self):
        return self.template

    def insert(self):
        test_polymer = ''
        for i in range(len(self.template) - 1):
            pair = self.template[i:i + 2]
            test_polymer += f'{self.template[i]}{self.insertion[pair]}'
        test_polymer += self.template[-1]
        self.template = test_polymer
        return self

    def difference(self):
        most, *_, least = Counter(self.template).most_common()
        return most[1] - least[1]


def main():
    with open("input.txt", "r") as file:
        polymer = Polymer(list(file.read().splitlines()))
        for _ in range(10):
            polymer.insert()
    print(polymer.difference())


if __name__ == '__main__':
    main()
