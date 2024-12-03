from itertools import groupby
from dataclasses import dataclass

from tqdm import tqdm
from data_loader import load_input


class Day13():

    def parse(self, input: str):
        patterns = []
        pattern = []
        for row in input.splitlines():
            if row == "":
                patterns.append(pattern)
                pattern = []
                continue
            pattern.append(row)
        patterns.append(pattern)
        self.patterns = patterns

    def solvePart1(self) -> int:
        vertical = 0
        horizontal = 0
        for p in tqdm(self.patterns):
            max_v = 0
            max_h = 0
            for i in range(len(p)):
                h = cnt_reflections_horizontal(p, i)
                max_h = h if h > max_h else max_h
            for i in range(len(p[0])):
                v = cnt_reflection_vertical(p, i)
                max_v = v if v > max_v else max_v
            if max_v > max_h:
                vertical += max_v
            else:
                horizontal += max_h
        return horizontal * 100 + vertical

    def solvePart2(self) -> int:
        return 0


def cnt_reflection_vertical(pattern: list[str], line: int) -> int:
    max_reflection = 0
    row_len = len(pattern[0])
    for offset in range(line+1):
        top_idx = line - offset
        bot_idx = line + offset + 1
        if bot_idx >= row_len or top_idx < 0:
            max_reflection = max_reflection if max_reflection > offset else offset
            break
        not_equal = False
        for rc in range(len(pattern)):
            top = pattern[rc][top_idx]
            bot = pattern[rc][bot_idx]
            if top != bot:
                not_equal = True
                break
        if not_equal:
            break
    return max_reflection + 1


def cnt_reflections_horizontal(pattern: list[str], line: int):
    max_reflection = 0
    row_len = len(pattern)
    for offset in range(line+1):
        top_idx = line - offset
        bot_idx = line + offset + 1
        if bot_idx >= row_len or top_idx < 0:
            max_reflection = max_reflection if max_reflection > offset else offset
            break
        top = pattern[top_idx]
        bot = pattern[bot_idx]
        if top != bot:
            break

    return max_reflection + 1


# if __name__ == '__main__':
    # d = Day13()
    # d.parse(load_input(13, 1))
    # print("### PART 1 ####")
    # print(d.patterns)
    # # print(cnt_reflection_vertical(d.patterns[0], 4))
    # # print(cnt_reflections_horizontal(d.patterns[1], 3))
    # print(d.solvePart1())
    # print("### PART 2 ###")
    # # print(d.solvePart2())


def find_mirror(group):
    for i in range(1, len(group)):
        above = group[:i][::-1]
        below = group[i:]

        if all(a == b for a, b in zip(above, below)):
            return i

    return 0


lines = load_input(13, 1).splitlines()

groups = [tuple(group)
          for not_empty, group in groupby(lines, bool) if not_empty]

res = 0
for group in groups:
    res += find_mirror(group) * 100
    res += find_mirror(tuple(zip(*group)))

print(res)


def find_mirror(group):
    for i in range(1, len(group)):
        above = group[:i][::-1]
        below = group[i:]
        if sum(sum(a != b for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return i

    return 0


lines = load_input(13, 1).splitlines()

groups = [tuple(group)
          for not_empty, group in groupby(lines, bool) if not_empty]

res = 0
for group in groups:
    res += find_mirror(group) * 100
    res += find_mirror(tuple(zip(*group)))

print(res)
