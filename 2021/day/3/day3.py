"""
Day 3
"""


def main():
    with open("input.txt", "r") as file:
        conditions = [element for element in file.read().splitlines()]
    # Find most frequent binary across each column
    gamma, epsilon = '', ''
    for i in range(len(conditions[0])):
        test = [condition[i] for condition in conditions]
        gamma += max(test, key=test.count)
        epsilon += min(test, key=test.count)
    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    main()
