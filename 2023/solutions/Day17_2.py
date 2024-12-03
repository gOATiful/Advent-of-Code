from data_loader import load_input


lines = load_input(17, 0).splitlines()


start = (0, 0)
goal = (len(lines[0]), len(lines))


def d(x: tuple) -> int:
    return int(lines[x[1]][x[0]])


def h(node: tuple):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


openSet = {start}
cameFrom = {}
gScore = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        node = (x, y)
        gScore[node] = float("inf")
gScore[start] = d(start)

fScore = {}
for y in range(len(lines)):
    for x in range(len(lines[0])):
        node = (x, y)
        fScore[node] = float("inf")
fScore[start] = h(start)


def lowest_fScore_node():
    lowest_score = float("inf")
    node = None
    for i in openSet:
        if fScore[i] < lowest_score:
            node = i
            lowest_score = fScore[i]
    return node


def get_neighbors(x: tuple, lines: list[str]):
    n = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = (x[0] + d[0], x[1] + d[1])
        if new_x[0] >= 0 and new_x[0] < len(lines[0]) and new_x[1] >= 0 and new_x[1] < len(lines):
            n.append(new_x)
    return n


def reconstruct_path(cameFrom: dict, current: tuple):
    path = [current]
    while current != None:
        current = cameFrom.get(current)
        path.insert(0, current)
    return path


while len(openSet) != 0:
    current = lowest_fScore_node()
    if current == goal:
        print(reconstruct_path(cameFrom, current))
    openSet.remove(current)
    for n in get_neighbors(current, lines):
        tentative_gScore = gScore[current] + d(n)
        if tentative_gScore < gScore[n]:
            cameFrom[n] = current
            gScore[n] = tentative_gScore
            fScore[n] = tentative_gScore + h(n)
            if n not in openSet:
                openSet.add(n)
