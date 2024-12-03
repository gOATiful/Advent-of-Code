
from collections import deque
from data_loader import load_input

lines = load_input(20, 1).splitlines()

broadcaster = []
stations = {}

for l in lines:
    l_split = l.split("->")
    station = l_split[0].strip()
    receivers = [x.strip() for x in l_split[1].split(",")]
    if station == "broadcaster":
        broadcaster = receivers
        continue
    type = station[0]
    name = station[1:]
    stations[name] = [type, False if type == "%" else {}, receivers]


# get inputs for conjunctions
for name, (_, _, receivers) in stations.items():
    for r in receivers:
        if r in stations and stations[r][0] == "&":
            stations[r][1][name] = False

print(stations)


low = 1000
high = 0

for _ in range(1000):
    queue = deque(["broadcaster", target, False] for target in broadcaster)

    while queue:
        name, target, pulse = queue.popleft()

        if pulse:
            high += 1
        else:
            low += 1

        if target not in stations:
            continue

        module = stations[target]

        if module[0] == "%":
            if pulse:
                continue

            module[1] = not module[1]
            new_pulse = module[1]
        else:
            module[1][name] = pulse
            new_pulse = not all(module[1].values())

        for destination in module[2]:
            queue.append((target, destination, new_pulse))

print(low * high)
