from data_loader import load_input
import re

input = load_input(15, 1)


def calc_hash(input: str) -> int:
    hash = 0
    for c in input:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


def solve_part1(input: str):
    input = input.split(",")
    hashes = [0 for _ in range(len(input))]
    for i, v in enumerate(input):
        hashes[i] = calc_hash(v)
    print(sum(hashes))


def contains_lens(name: str, lst: list):
    for i, l in enumerate(lst):
        if name in l:
            return i
    return -1


def calc_focussing_power(hashmap: dict) -> int:
    power = 0
    for boxidx, lenses in hashmap.items():
        for i, lens in enumerate(lenses):
            focal = lens.split(" ")[1]
            lens_power = (boxidx + 1) * (i + 1) * int(focal)
            power += lens_power
    return power


def solve_part2(input: str):
    input = input.split(",")
    hashmap = {x: [] for x in range(256)}
    for lens in input:
        s = re.split("[-=]", lens)
        label = s[0]
        hash = calc_hash(label)
        if "-" in lens:
            box = hashmap[hash]
            idx = contains_lens(label, box)
            if idx >= 0:
                box.pop(idx)
        elif "=" in lens:
            box = hashmap[hash]
            idx = contains_lens(label, box)
            focal = s[1]
            lens_in_box = f"{label} {focal}"
            if idx >= 0:
                box[idx] = lens_in_box
            else:
                box.append(lens_in_box)

    return calc_focussing_power(hashmap)


print(solve_part2(input))
