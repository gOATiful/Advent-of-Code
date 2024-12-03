from data_loader import load_input
import sys
from tqdm import tqdm
sys.setrecursionlimit(100_000) 

lines = load_input(16, 1).splitlines()


history = []


def is_outbound(x: int, y: int, lines: list[str]):
    return x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines)


def beam_step(lines: list[str], position: tuple, dir: tuple):
    x = position[0]
    y = position[1]

    if is_outbound(x, y, lines) or (position, dir) in history:
        return
    history.append((position, dir))
    cell = lines[y][x]
    if cell == "|":
        beam_step(lines, (x, y-1), (0, -1))
        beam_step(lines, (x, y+1), (0, 1))
    elif cell == "-":
        beam_step(lines, (x-1, y), (-1, 0))
        beam_step(lines, (x+1, y), (1, 0))
    elif cell == "/":
        dir = (-dir[1], -dir[0])
        beam_step(lines, (x + dir[0], y + dir[1]), dir)
    elif cell == "\\":
        dir = (dir[1], dir[0])
        beam_step(lines, (x + dir[0], y + dir[1]), dir)
    else:
        beam_step(lines, (x + dir[0], y + dir[1]), dir)


def solve_part1(lines: list[str]) -> int:
    start = (0, 0)
    dir = (1, 0)
    beam_step(lines, start, dir)
    print(len(history))
    energized = len(set(map(lambda x: x[0], history)))
    print(energized)
    return energized


def solve_part2(lines: list[str]) -> int:
    max_energy = 0
    # starting from top
    for x in tqdm(range(len(lines[0]))):
        start = (x, 0)
        dir = (0, 1)
        beam_step(lines, start, dir)
        energized = len(set(map(lambda x: x[0], history)))
        max_energy = energized if energized > max_energy else max_energy
        history.clear()
    # starting from bottom
    for x in tqdm(range(len(lines[0]))):
        start = (x, len(lines)-1)
        dir = (0, -1)
        beam_step(lines, start, dir)
        energized = len(set(map(lambda x: x[0], history)))
        max_energy = energized if energized > max_energy else max_energy
        history.clear()
    for y in tqdm(range(len(lines))):
        start = (0, y)
        dir = (1, 0)
        beam_step(lines, start, dir)
        energized = len(set(map(lambda x: x[0], history)))
        max_energy = energized if energized > max_energy else max_energy
        history.clear()
    for y in tqdm(range(len(lines))):
        start = (len(lines[0])-1, y)
        dir = (-1, 0)
        beam_step(lines, start, dir)
        energized = len(set(map(lambda x: x[0], history)))
        max_energy = energized if energized > max_energy else max_energy
        history.clear()

    return max_energy


# solve_part1(lines)
print(solve_part2(lines))
