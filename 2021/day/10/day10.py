"""
Day 10
"""
from collections import namedtuple
import statistics

CloseChunk = namedtuple('CloseChunk', 'illegal completion')

open_chunk = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

close_chunk = {
    ')': CloseChunk(3, 1),
    ']': CloseChunk(57, 2),
    '}': CloseChunk(1197, 3),
    '>': CloseChunk(25137, 4)
}


def chunk_check(line):
    prev_chunks = ''
    for chunk in line:
        if chunk in '([{<':
            prev_chunks += chunk
        elif chunk in ')]}>':
            if chunk != open_chunk[prev_chunks[-1]]:
                return CloseChunk(close_chunk[chunk].illegal, 0)
            prev_chunks = prev_chunks[:-1]
    complete_chunk = [open_chunk[prev] for prev in prev_chunks]
    completion = 0
    for chunk in reversed(complete_chunk):
        completion *= 5
        completion += close_chunk[chunk].completion
    return CloseChunk(0, completion)


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()
    print(sum(chunk_check(line).illegal for line in lines))  # Part 1
    print(statistics.median(
        sorted(chunk_check(line).completion for line in lines if chunk_check(line).completion)))  # Part 2


if __name__ == '__main__':
    main()
