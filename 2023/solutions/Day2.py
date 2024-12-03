from dataclasses import dataclass
from functools import reduce
from data_loader import load_input


@dataclass
class Game():
    id: int
    sets: list

    def is_possible(self, bag) -> bool:
        for s in self.sets:
            for k, v in s.items():
                if k not in bag.keys() or v > bag[k]:
                    return False
        return True


def parse_set(set: list) -> map:
    ret_set = {}
    for item in set:
        for color in ["green", "blue", "red"]:
            if color in item:
                cnt = int(item.replace(f" {color}", ""))
                ret_set[color] = cnt
                break
    return ret_set


def parse(line: str) -> Game:
    game_split = line.split(":")
    id = int(game_split[0].replace("Game ", ""))
    set_lists = game_split[1].split(";")
    sets = [parse_set(x.split(",")) for x in set_lists]
    return Game(id, sets)


class Day2():
    part1_example_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

    part1_example_solution = 8

    part2_example_solution = 2286

    def parseInput(self, input: str):
        self.games = [parse(x)for x in input.splitlines()]

    def solvePart1(self, bag) -> int:
        items = [x.id for x in self.games if x.is_possible(bag=bag)]
        return sum(items)

    def solvePart2(self) -> int:
        powers = []
        for g in self.games:
            min_set = {}
            for s in g.sets:
                for k, v in s.items():
                    if k not in min_set.keys():
                        min_set[k] = v
                    else:
                        if min_set[k] < v:
                            min_set[k] = v
            powers.append(reduce(lambda a, b: a * b, min_set.values()))
        return sum(powers)


if __name__ == '__main__':
    d = Day2()
    d.parseInput(d.part1_example_input)
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    print(d.solvePart1(bag))

    d.parseInput(load_input(2))
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    print(d.solvePart1(bag))
    # d.parseInput(d.part1_example_input)
    print(d.solvePart2())
