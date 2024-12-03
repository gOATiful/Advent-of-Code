from dataclasses import dataclass

from tqdm import tqdm
from data_loader import load_input


@dataclass
class Card():
    name: str
    winning: list[int]
    actual: list[int]

    def calc_hits(self) -> int:
        winning = set(self.winning)
        actual = set(self.actual)
        overlap = winning & actual
        return len(overlap)


class Day4():

    def parse(self, input: str):
        self.cards = []
        for row in input.splitlines():
            name_split = row.split(":")
            name = name_split[0]
            card_split = name_split[1].split("|")
            winning = [int(x) for x in card_split[0].split(" ") if len(x) > 0]
            actual = [int(x) for x in card_split[1].split(" ") if len(x) > 0]
            self.cards.append(Card(name, winning, actual))

    def solvePart1(self) -> int:
        points = 0
        for c in self.cards:
            hits = c.calc_hits()
            p = int(2 ** (hits-1))
            points += p
        return points

    def solvePart2(self) -> int:
        idx = 0
        while idx < len(self.cards):
            c = self.cards[idx]
            hits = c.calc_hits()
            print(f"{c.name} adds {hits} cards")
            for i in range(hits):
                self.cards.append(self.cards[idx + 1 + i])
            idx += 1
        print(len(self.cards))


if __name__ == '__main__':
    d = Day4()
    d.parse(load_input(4, 0))
    print("### PART 1 ####")
    print(d.solvePart1())
    print("### PART 2 ###")
    print(d.solvePart2())
