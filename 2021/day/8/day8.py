"""
Day 8
"""
import itertools


class SevenSegment:

    def __init__(self, line):
        self.patterns, self.output = line.split('|')
        self.patterns = [''.join(sorted(pattern)) for pattern in self.patterns.split(' ') if pattern]
        self.digits = self.determine_digits()
        self.output = [''.join(sorted(output)) for output in self.output.split(' ') if output]

    def determine_digits(self):
        for key in [''.join(p) for p in itertools.permutations('abcdefg')]:
            digits = {
                0: f'{key[0:3]}{key[4:7]}',
                1: f'{key[2]}{key[5]}',
                2: f'{key[0]}{key[2:5]}{key[6]}',
                3: f'{key[0]}{key[2:4]}{key[5:7]}',
                4: f'{key[1:4]}{key[5]}',
                5: f'{key[0:2]}{key[3]}{key[5:7]}',
                6: f'{key[0:2]}{key[3:7]}',
                7: f'{key[0]}{key[2]}{key[5]}',
                8: f'{key}',
                9: f'{key[0:4]}{key[5:7]}'
            }
            if sorted([''.join(sorted(pattern)) for pattern in digits.values()]) == sorted(self.patterns):
                return digits

    def sum_easy_digits(self):
        return sum(len(output) in [2, 4, 3, 7] for output in self.output)

    def value_all_outputs(self):
        output_value = {''.join(sorted(v)): str(k) for k, v in self.digits.items()}
        return int(
            f'{output_value[self.output[0]]}{output_value[self.output[1]]}{output_value[self.output[2]]}{output_value[self.output[3]]}'
        )


def main():
    with open("input.txt", "r") as file:
        seven_segments = [SevenSegment(line) for line in file.read().splitlines()]
    print(sum(segment.sum_easy_digits() for segment in seven_segments))  # Part 1
    print(sum(segment.value_all_outputs() for segment in seven_segments))  # Part 2


if __name__ == '__main__':
    main()
