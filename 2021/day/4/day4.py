"""
Day 4
"""
import operator

import json
import copy
from collections import OrderedDict


class BingoCard:
    """Stores bingo card as an object
    """

    def __init__(self, card: list[list[str]]):
        self.card = card
        self.bingo = {letter: row for letter, row in zip('BINGO', card)}

    def __repr__(self):
        return '\n'.join('\t'.join(row) for row in self.card)

    def __str__(self):
        return '\n'.join('\t'.join(row) for row in self.card)

    @staticmethod
    def check_line(values):
        for line in values:
            if all(val == 'X' for val in line):
                return True

    def check_win(self):
        # down_right = all(self.bingo[key][idx] == 'X' for idx, key in enumerate(self.bingo))
        # up_right = all(self.bingo[key][idx] == 'X' for idx, key in zip(reversed(range(5)), self.bingo))
        horz = self.check_line(self.bingo.values())
        vert = self.check_line(zip(*self.bingo.values()))
        return any([horz, vert])

    def draw(self, draw):
        """
        Mark draw in bingo board
        :param draw:
        :return:
        """
        for letter in self.bingo:
            for i, number in enumerate(self.bingo[letter]):
                if number == draw:
                    self.bingo[letter][i] = 'X'
        return self.check_win()

    def final_score(self, draw):
        """
        Sum of all unclaimed numbers
        :return:
        """
        return sum(int(num) for lst in self.bingo.values() for num in lst if num != 'X') * draw


def main():
    with open("input.txt", "r") as file:
        cards = list(file.read().splitlines())
    # Grab Draw
    draw_order = cards.pop(0).split(',')
    # Pull out remainder
    cards = [element.split() for element in cards if element]
    # Create Bingo Cards
    cards = [BingoCard(cards[i:i + 5]) for i in range(0, len(cards), 5)]
    for draw in draw_order:
        print(draw)
        for card in cards:
            if card.draw(draw):
                print(card)
                print(card.final_score(int(draw)))
                exit()


if __name__ == '__main__':
    main()
