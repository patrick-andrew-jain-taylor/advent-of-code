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

    def _insert(self, polymer, times):
        if not times:
            return Counter(polymer[0])
        times -= 1
        return \
            self._insert(f'{polymer[0]}{self.insertion[polymer]}', times) + \
            self._insert(f'{self.insertion[polymer]}{polymer[1]}', times)

    def insert(self, times=1):
        count = Counter()
        polymers = [self.template[i:i + 2] for i in range(len(self.template) - 1)]
        for polymer in polymers:
            count += self._insert(polymer, times)
        return count + Counter(self.template[-1])


def main():
    with open("test.txt", "r") as file:
        polymer = Polymer(list(file.read().splitlines()))
    polymer.insert(40)


if __name__ == '__main__':
    main()
