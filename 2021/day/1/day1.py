"""
How many measurements are larger than the previous measurement?
"""


def main():
    """

    :return: Number of measurements larger than previous
    """
    # Load txt file to list
    with open("input.txt", "r") as file:
        measurements = file.read().splitlines()
    # Loop over list
    return sum(
        second > first
        for first, second
        in zip(
            measurements[:-2],
            measurements[1:]
        )
    )


if __name__ == '__main__':
    main()
