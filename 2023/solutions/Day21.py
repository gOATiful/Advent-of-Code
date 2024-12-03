

from data_loader import load_input


lines = load_input(21, 0).splitlines()
garden_map = []
start = ()
for y, l in enumerate(lines):
    line = []
    for x, c in enumerate(l):
        line.append(c)
        if c == "S":
            start = (x, y)
    garden_map.append(line)


def get_cell(pos: tuple):
    if pos[0] < 0 or pos[0] >= len(garden_map[0]) or pos[1] < 0 or pos[1] >= len(garden_map):
        return None
    return garden_map[pos[1]][pos[0]]


def step(pos: tuple, steps_left: int):
    print("\n".join(["".join(l) for l in garden_map]))
    if steps_left == 0:
        return
    cell = get_cell(pos)
    has_next_cell = False
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        next_cell = get_cell(next_pos)
        if next_cell and next_cell != "#":
            has_next_cell = True
            garden_map[next_pos[1]][next_pos[0]] = "O"
            step(next_pos, steps_left - 1)

    if has_next_cell and cell in "OS":
        garden_map[pos[1]][pos[0]] = "."


step(start, 6)
