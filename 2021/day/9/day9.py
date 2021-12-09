"""
Day 9
"""


def main():
    with open("input.txt", "r") as file:
        heatmap = [[int(digit) for digit in line] for line in file.read().splitlines()]
    heatsum = 0
    for i in range(len(heatmap)):
        for j in range(len(heatmap[i])):
            if i == 0 and j == 0:  # Down and Right
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][
                    j + 1] else 0
            elif i == 0 and j == len(heatmap[i]) - 1:  # Down and Left
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][
                    j - 1] else 0
            elif i == len(heatmap) - 1 and j == 0:  # Up and Right
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][
                    j + 1] else 0
            elif i == len(heatmap) - 1 and j == len(heatmap[i]) - 1:  # Up and Left
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][
                    j - 1] else 0
            elif i == 0:  # Down, Left, Right
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][
                    j - 1] and heatmap[i][j] < heatmap[i][j + 1] else 0
            elif i == len(heatmap) - 1:  # Up, Left, Right
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][
                    j - 1] and heatmap[i][j] < heatmap[i][j + 1] else 0
            elif j == 0:  # Up, Down, Right
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i + 1][
                    j] and heatmap[i][j] < heatmap[i][j + 1] else 0
            elif j == len(heatmap[i]) - 1:  # Up, Down, Left
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i + 1][
                    j] and heatmap[i][j] < heatmap[i][j - 1] else 0
            else:  # Up, Left, Down, Right
                heatsum += heatmap[i][j] + 1 if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][
                    j - 1] and heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][j + 1] else 0
    print(heatsum)


if __name__ == '__main__':
    main()
