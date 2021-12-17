"""
Day 14
"""
from collections import Counter


class Polymer:
    def __init__(self, formula):
        self.template = formula[0]
        self.insertion = {k: v for rule in formula[2:] for k, v in dict([rule.split(' -> ')]).items()}

    def __repr__(self):
        return self.template

    def __str__(self):
        return self.template

    def insert(self, times=1):
        polymers = [self.template[i:i + 2] for i in range(len(self.template) - 1)]
        pair_count = Counter(polymers)
        elem_count = Counter(self.template)
        for _ in range(times):
            for key, value in list(pair_count.items()):
                elem = self.insertion[key]
                elem_count[elem] += value
                pair_count[key] -= value
                pair_count[f'{key[0]}{elem}'] += value
                pair_count[f'{elem}{key[1]}'] += value
        most, *_, least = elem_count.most_common()
        return most[1] - least[1]


def main():
    with open("input.txt", "r") as file:
        polymer = Polymer(list(file.read().splitlines()))
    print(polymer.insert(10))  # Part 1
    print(polymer.insert(40))  # Part 2


if __name__ == '__main__':
    main()
