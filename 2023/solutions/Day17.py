
from data_loader import load_input


lines = load_input(17, 0).splitlines()


M = set()
dist = {}
predecessors = {}

for y in range(len(lines)):
    for x in range(len(lines[0])):
        node = (x, y)
        M.add(node)
        dist[node] = float("inf")
start = (0, 0)
dist[start] = int(lines[start[1]][start[0]])


def get_min_node(dist: dict, M: set):
    min = float("inf")
    min_node = None
    for n in list(M):
        v = dist[n]
        if v < min:
            min_node = n
    return min_node


def get_neighbors(x: tuple, lines: list[str]):
    n = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = (x[0] + d[0], x[1] + d[1])
        if new_x[0] >= 0 and new_x[0] < len(lines[0]) and new_x[1] >= 0 and new_x[1] < len(lines):
            n.append(new_x)
    return n


def get_distance(pos: tuple, pre: tuple) -> float:
    backtrack_dir = (pre[0] - pos[0], pre[1] - pos[1])
    p = pre
    in_line = 1
    for _ in range(2):
        backtrack_node = predecessors.get(p)
        p = (p[0] + backtrack_dir[0], p[1] + backtrack_dir[1])
        if backtrack_node == p:
            in_line += 1
    if in_line == 3:
        return float("inf")
    return int(lines[pos[1]][pos[0]])


while len(M) != 0:
    print(len(M))
    x = get_min_node(dist, M)
    M.remove(x)
    n_all = get_neighbors(x, lines)
    for n in [n for n in n_all if n in M]:
        new_dist = dist[x] + get_distance(n, x)
        if new_dist <= dist[n]:  # add 3 in a row
            dist[n] = new_dist
            predecessors[n] = x


current_node = (len(lines[0])-1, len(lines)-1)

heat = 0
heat_map = [["." for _ in range(len(lines[0]))] for _ in range(len(lines))]
while current_node != None:
    heat += int(lines[current_node[1]][current_node[0]])
    heat_map[current_node[1]][current_node[0]] = "X"
    current_node = predecessors.get(current_node)

print(heat)
for l in heat_map:
    print("".join(l))
print(dist)