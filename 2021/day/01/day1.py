"""
Day 1
"""


def difference(measures):
    return sum(
        second > first
        for first, second
        in zip(
            measures[:-1],
            measures[1:]
        )
    )


def sum_three(measures):
    return [
        first + second + third
        for first, second, third
        in zip(
            measures[:-2],
            measures[1:-1],
            measures[2:]
        )
    ]


def part1(measures):
    """
    How many measurements are larger than the previous measurement?
    :param measures: Data to be differed.
    :return: Number of measurements larger than previous
    """
    return difference(measures)


def part2(measures):
    """
    How many sums are larger than the previous sum?
    :param measures: Data to be differed.
    :return: Number of sums larger than previous
    """
    return difference(sum_three(measures))


def main():
    # Load txt file to list
    with open("input.txt", "r") as file:
        measurements = [int(element) for element in file.read().splitlines()]
    # Part 1
    print(part1(measurements))
    # Part 2
    print(part2(measurements))


if __name__ == '__main__':
    main()
