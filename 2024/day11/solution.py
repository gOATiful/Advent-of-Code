from functools import cache


def load_input(path: str) -> list[str]:
    with open(path) as infile:
        return infile.read().splitlines()


puzzle_input = load_input("2024/day11/example.txt")[0]
# puzzle_input = load_input("input.txt")[0]
stones = [int(x) for x in puzzle_input.split(" ")]


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    stone_str = str(stone)
    str_len = len(stone_str)
    mid = str_len//2
    if str_len % 2 == 0:
        return count(int(stone_str[:mid]), steps - 1) + count(int(stone_str[mid:]), steps-1)
    return count(stone * 2024, steps-1)


print(sum(count(stone, 25) for stone in stones))