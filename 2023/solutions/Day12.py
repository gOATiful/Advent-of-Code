from functools import cache
from dataclasses import dataclass
from tqdm import tqdm
from data_loader import load_input


@dataclass
class Record():
    condition: str
    groups: list[int]


def parse_records(input: str) -> list[Record]:
    ret = []
    for row in input.splitlines():
        row_split = row.split(" ")
        groups = [int(x) for x in row_split[1].split(",")]
        condition = row_split[0]
        ret.append(Record(condition, groups))
    return ret


def parse_records2(input: str) -> list[Record]:
    ret = parse_records(input)
    for r in ret:
        r.condition = "?".join([r.condition for _ in range(5)])
        r.groups = [x for _ in range(5) for x in r.groups]

    return ret


def is_valid(inp: str, groups: list[int]) -> bool:
    cmp_group = [len(x) for x in inp.split(".") if len(x) > 0]
    return cmp_group == groups


def can_be_valid(inp: str, groups: list[int]) -> bool:
    cmp_group = [x for x in inp.split(".") if len(x) > 0]
    for i, e in enumerate(groups):
        if i >= len(cmp_group):
            break
        if "?" in cmp_group[i]:
            return True
        if len(cmp_group[i]) != e:
            return False
    return True


def backtracking(condition: str, groups: list[int], idx=0) -> int:
    ret = 0
    if len(condition) == idx:
        ret = 1 if is_valid(condition, groups) else 0
    elif condition[idx] != "?":
        idx += 1
        ret += backtracking(condition, groups, idx)
    else:
        for c in [".", "#"]:
            backtracking_condition = condition[:idx] + c + condition[idx+1:]
            if can_be_valid(backtracking_condition, groups):
                ret += backtracking(backtracking_condition, groups, idx)
    return ret


class Day12():

    def solvePart1(self, input: str) -> int:
        records = parse_records(input)
        ret = 0
        for r in tqdm(records):
            ret += backtracking(r.condition, r.groups)
        return ret

    def solvePart2(self, input: str) -> int:
        records = parse_records2(input)
        ret = 0
        for r in tqdm(records):
            ret += backtracking(r.condition, r.groups)
        return ret


# if __name__ == '__main__':
#    d = Day12()
    # print(backtracking("?###????????", [3, 2, 1]))
    # print(d.solvePart1(load_input(12, 1)))
    # print(backtracking("????.######..#####.", [1, 6, 5]))
#    print(d.solvePart2(load_input(12, 0)))


lines = load_input(12, 1).splitlines()

@cache
def check_pattern(line, numbers):
    if not line:
        return not numbers

    if not numbers:
        return "#" not in line

    res = 0

    if line[0] in ".?":
        res += check_pattern(line[1:], numbers)

    if line[0] in "#?":
        if (
            numbers[0] <= len(line)
            and "." not in line[: numbers[0]]
            and (numbers[0] == len(line) or line[numbers[0]] != "#")
        ):
            res += check_pattern(line[numbers[0] + 1:], numbers[1:])

    return res


res = 0
for line in lines:
    spring, condition = line.split()
    condition = tuple(map(int, condition.split(",")))
    res += check_pattern("?".join([spring] * 5), condition * 5)

print(res)
