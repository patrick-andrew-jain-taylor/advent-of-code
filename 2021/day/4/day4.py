"""
Day 4
"""
import copy


class BingoCard:
    """Stores bingo card as an object
    """

    def __init__(self, card: list[list[str]]):
        self.card = card
        self.bingo = dict(zip('BINGO', copy.deepcopy(card)))

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
        return draw

    def final_score(self, draw):
        """
        Sum of all unclaimed numbers
        :return:
        """
        return sum(int(num) for lst in self.bingo.values() for num in lst if num != 'X') * draw


def part1(draw_order, cards):
    for draw in draw_order:
        for card in cards:
            card.draw(draw)
            if card.check_win():
                print(card.final_score(int(draw)))
                exit()


def part2(draw_order, cards):
    for draw in draw_order:
        # Draw First
        for card in cards:
            card.draw(draw)
        # Remove Second
        for card in cards:
            if card.check_win():
                cards.remove(card)
                if not cards:
                    print(card.final_score(int(draw)))
                    exit()
    exit(1)


def main():
    with open("input.txt", "r") as file:
        cards = list(file.read().splitlines())
    # Grab Draw
    draw_order = cards.pop(0).split(',')
    # Pull out remainder
    cards = [element.split() for element in cards if element]
    # Create Bingo Cards
    cards = [BingoCard(cards[i:i + 5]) for i in range(0, len(cards), 5)]
    # part1(draw_order, cards)
    part2(draw_order, cards)


if __name__ == '__main__':
    main()
