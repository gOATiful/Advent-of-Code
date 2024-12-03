from enum import Enum
from data_loader import load_input
from tqdm import tqdm

lines = tuple(load_input(14, 1).splitlines())


class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4


def slide(input: list[str], dir: Direction):
    new_input = ["" for _ in input]
    if dir == Direction.NORTH:
        for i in range(len(input[0])):
            row = "".join([r[i] for r in input])
            split_rocks = row.split("#")
            sort_rocks = ["".join(sorted(x, reverse=True))
                          for x in split_rocks]
            reverse_split = "#".join(sort_rocks)
            for j, c in enumerate(reverse_split):
                new_input[j] += c
    elif dir == Direction.SOUTH:
        for i in range(len(input[0])):
            row = "".join([r[i] for r in input])
            split_rocks = row.split("#")
            sort_rocks = ["".join(sorted(x)) for x in split_rocks]
            reverse_split = "#".join(sort_rocks)
            for j, c in enumerate(reverse_split):
                new_input[j] += c
    elif dir == Direction.EAST:
        for i, row in enumerate(input):
            split_rocks = row.split("#")
            sort_rocks = ["".join(sorted(x)) for x in split_rocks]
            reverse_split = "#".join(sort_rocks)
            new_input[i] = reverse_split
    elif dir == Direction.WEST:
        for i, row in enumerate(input):
            split_rocks = row.split("#")
            sort_rocks = ["".join(sorted(x, reverse=True))
                          for x in split_rocks]
            reverse_split = "#".join(sort_rocks)
            new_input[i] = reverse_split
    return new_input


def full_cycle(input: list[str]) -> list[str]:
    for d in [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]:
        input = slide(input, d)

    return input


cache = {}


def solve_part2(input: list[str]) -> int:
    total = 1000000000
    i = 0
    with tqdm(total=total) as pbar:
        while (i < total):
            key = "\n".join(input)
            if key in cache.keys():
                next_step = cache[key][-1]
                next_step = full_cycle(next_step)  # add a step
                cache[key].append(next_step)
                i += len(cache[key])
                pbar.update(len(cache[key]))
            else:
                next_step = full_cycle(input)
                cache[key] = [next_step]
                pbar.update(1)
                i += 1
            input = next_step

    return get_total_load(input)


def get_total_load(input: list[str]) -> int:
    loads = [0 for _ in range(len(input))]
    load_val = len(input)
    for i, row in enumerate(input):
        for c in row:
            if c == "O":
                loads[i] += load_val
        load_val -= 1
    return sum(loads)


def solve_part1(input: list[str]) -> int:
    turn = slide(input, Direction.NORTH)
    return get_total_load(turn)


# print(solve_part1(lines))
# print(solve_part2(lines))