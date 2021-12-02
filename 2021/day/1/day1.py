"""
"""


def part1(measures):
    """
    How many measurements are larger than the previous measurement?
    :param measures: Data to be differed.
    :return: Number of measurements larger than previous
    """
    return difference(measures)


def difference(measures):
    return sum(
        second > first
        for first, second
        in zip(
            measures[:-1],
            measures[1:]
        )
    )


if __name__ == '__main__':
    # Load txt file to list
    with open("input.txt", "r") as file:
        measurements = [int(element) for element in file.read().splitlines()]
    print(part1(measurements))
