"""
Day 9
"""
import heapq
import math


def determine_low_points(heatmap):
    heatlist = []
    for i in range(len(heatmap)):
        for j in range(len(heatmap[i])):
            if i == 0 and j == 0:  # Down and Right
                if heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][j + 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif i == 0 and j == len(heatmap[i]) - 1:  # Down and Left
                if heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][j - 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif i == len(heatmap) - 1 and j == 0:  # Up and Right
                if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][j + 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif i == len(heatmap) - 1 and j == len(heatmap[i]) - 1:  # Up and Left
                if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][j - 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif i == 0:  # Down, Left, Right
                if heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][j - 1] and heatmap[i][j] < \
                        heatmap[i][j + 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif i == len(heatmap) - 1:  # Up, Left, Right
                if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][j - 1] and heatmap[i][j] < \
                        heatmap[i][j + 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif j == 0:  # Up, Down, Right
                if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < \
                        heatmap[i][j + 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif j == len(heatmap[i]) - 1:  # Up, Down, Left
                if heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i + 1][j] and heatmap[i][j] < \
                        heatmap[i][j - 1]:
                    heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
            elif heatmap[i][j] < heatmap[i - 1][j] and heatmap[i][j] < heatmap[i][j - 1] and heatmap[i][j] < \
                    heatmap[i + 1][j] and heatmap[i][j] < heatmap[i][j + 1]:
                heatlist.append({'i': i, 'j': j, 'risk': heatmap[i][j] + 1})
    return heatlist


def walk_basin(heatmap, i, j, size):
    heatmap[i][j] = 9
    size += 1
    if i == 0 and j == 0:  # Down and Right
        if heatmap[i + 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i + 1, j, size)
        if heatmap[i][j + 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j + 1, size)
    elif i == 0 and j == len(heatmap[i]) - 1:  # Down and Left
        if heatmap[i + 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i + 1, j, size)
        if heatmap[i][j - 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j - 1, size)
    elif i == len(heatmap) - 1 and j == 0:  # Up and Right
        if heatmap[i - 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i - 1, j, size)
        if heatmap[i][j + 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j + 1, size)
    elif i == len(heatmap) - 1 and j == len(heatmap[i]) - 1:  # Up and Left
        if heatmap[i - 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i - 1, j, size)
        if heatmap[i][j - 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j - 1, size)
    elif i == 0:  # Down, Left, Right
        if heatmap[i + 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i + 1, j, size)
        if heatmap[i][j - 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j - 1, size)
        if heatmap[i][j + 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j + 1, size)
    elif i == len(heatmap) - 1:  # Up, Left, Right
        if heatmap[i - 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i - 1, j, size)
        if heatmap[i][j - 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j - 1, size)
        if heatmap[i][j + 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j + 1, size)
    elif j == 0:  # Up, Down, Right
        if heatmap[i - 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i - 1, j, size)
        if heatmap[i + 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i + 1, j, size)
        if heatmap[i][j + 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j + 1, size)
    elif j == len(heatmap[i]) - 1:  # Up, Down, Left
        if heatmap[i - 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i - 1, j, size)
        if heatmap[i + 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i + 1, j, size)
        if heatmap[i][j - 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j - 1, size)
    else:
        if heatmap[i - 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i - 1, j, size)
        if heatmap[i][j - 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j - 1, size)
        if heatmap[i + 1][j] != 9:
            heatmap, size = walk_basin(heatmap, i + 1, j, size)
        if heatmap[i][j + 1] != 9:
            heatmap, size = walk_basin(heatmap, i, j + 1, size)
    return heatmap, size


def determine_all_basins(heatmap, heatlist):
    for heat in heatlist:
        heatmap, heat['basin'] = walk_basin(heatmap, heat['i'], heat['j'], 0)
    return math.prod(heapq.nlargest(3, [heat['basin'] for heat in heatlist]))


def main():
    with open("input.txt", "r") as file:
        heatmap = [[int(digit) for digit in line] for line in file.read().splitlines()]
    heatlist = determine_low_points(heatmap)
    print(sum(heat['risk'] for heat in heatlist))  # Part 1
    print(determine_all_basins(heatmap, heatlist))  # Part 2


if __name__ == '__main__':
    main()
