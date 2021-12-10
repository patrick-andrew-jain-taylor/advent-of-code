"""
Day 3
"""


def part1(conditions):
    # Find most frequent binary across each column
    gamma, epsilon = '', ''
    for i in range(len(conditions[0])):
        test = [condition[i] for condition in conditions]
        gamma += max(test, key=test.count)
        epsilon += min(test, key=test.count)
    print(int(gamma, 2) * int(epsilon, 2))


def part2(conditions):
    # Process of elimination binaries
    # Oxygen
    oxygen = conditions
    for i in range(len(oxygen[0])):
        oxygen_digit = [condition[i] for condition in oxygen]
        oxygen_digit_max = max(oxygen_digit, key=oxygen_digit.count)
        oxygen_digit_min = min(oxygen_digit, key=oxygen_digit.count)
        oxygen = [condition for condition in oxygen if
                  condition[i] == (oxygen_digit_max != oxygen_digit_min and oxygen_digit_max or '1')]
        if len(oxygen) == 1:
            break
    # CO2
    co2 = conditions
    for i in range(len(co2[0])):
        co2_digit = [condition[i] for condition in co2]
        co2_digit_min = min(co2_digit, key=co2_digit.count)
        co2_digit_max = max(co2_digit, key=co2_digit.count)
        co2 = [condition for condition in co2 if
               condition[i] == (co2_digit_max != co2_digit_min and co2_digit_min or '0')]
        if len(co2) == 1:
            break
    print(int(oxygen[0], 2) * int(co2[0], 2))


def main():
    with open("input.txt", "r") as file:
        elements = list(file.read().splitlines())
    part1(elements)
    part2(elements)


if __name__ == '__main__':
    main()
