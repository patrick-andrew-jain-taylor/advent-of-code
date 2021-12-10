"""
Day 10
"""
from collections import namedtuple

OpenClose = namedtuple('OpenClose', 'open_chunk close_chunk value')

open_chunk = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

close_chunk = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def chunk_check(line):
    prev_chunks = ''
    for chunk in line:
        # print(prev_chunks)
        if chunk in '([{<':
            prev_chunks += chunk
        elif chunk in ')]}>':
            if chunk != open_chunk[prev_chunks[-1]]:
                return close_chunk[chunk]
            prev_chunks = prev_chunks[:-1]
    return 0


def main():
    with open("input.txt", "r") as file:
        print(sum(chunk_check(line) for line in file.read().splitlines()))


if __name__ == '__main__':
    main()
