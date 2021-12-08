"""
Day 8
"""


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    count = {
        1: 0,
        4: 0,
        7: 0,
        8: 0
    }
    for line in lines:
        patterns, output = line.split('|')
        for segment in output.split(' '):
            if len(segment) == 2:
                count[1] += 1
            elif len(segment) == 4:
                count[4] += 1
            elif len(segment) == 3:
                count[7] += 1
            elif len(segment) == 7:
                count[8] += 1
    print(sum(count.values()))


if __name__ == '__main__':
    main()
