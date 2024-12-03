from data_loader import load_input
import sys
lines = load_input(10, 1).splitlines()
sys.setrecursionlimit(1000000)

def get_starting_position(input: list[str]) -> tuple:
    for y, line in enumerate(input):
        if "S" in line:
            x = line.index("S")
            return (x, y)


def is_valid_move(dir, pipe_segment):
    valid_moves = {
        (1, 0): "-J7",
        (-1, 0): "-LF",
        (0, 1): "|LJ",
        (0, -1): "|F7",
    }
    return pipe_segment in valid_moves[dir]


def search_pipes(input: list[str], starting_position: tuple, stack=[]):
    p = starting_position
    best = 0
    for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_p = (p[0] + dir[0], p[1] + dir[1])
        if next_p[0] < 0 or next_p[0] >= len(input[0]) or next_p[1] < 0 or next_p[1] >= len(input):
            continue
        next_segment = input[next_p[1]][next_p[0]]
        if next_segment == "S" and len(stack) > 1:
            # start found!!! return
            return int(len(stack) / 2 + 0.5)
        if next_p not in stack and is_valid_move(dir, next_segment):
            stack.append(starting_position)
            ret = search_pipes(input, next_p, stack)
            best = ret if ret > best else best
    return best


starting_position = get_starting_position(lines)

print(search_pipes(lines, starting_position))
