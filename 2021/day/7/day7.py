"""
Day 7
"""


def main():
    with open("input.txt", "r") as file:
        crabs = file.read().strip().split(',')
    crabs = [int(crab) for crab in crabs]
    print(min(sum(abs(crab - distance) for distance in crabs) for crab in crabs))  # Part 1
    print(min(sum(sum(range(abs(crab - distance) + 1)) for crab in crabs) for distance in range(max(crabs))))  # Part 2


if __name__ == '__main__':
    main()
