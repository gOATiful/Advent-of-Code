from dataclasses import dataclass

from tqdm import tqdm
from data_loader import load_input


@dataclass
class AlmanacItem():
    source: str
    desination: str
    source_start: int
    source_end: int
    destination_start: int
    destination_end: int


class Day1():
    seeds: list
    almanac: list[AlmanacItem]

    src_dst_list = {
        "seed": "soil",
        "soil": "fertalizer",
        "fertalizer": "water",
        "water": "light",
        "light": "temperature",
        "temperature": "humidity",
        "humidity": "location"
    }

    def parse(self, input: str):
        lines = input.splitlines()
        seeds = [int(x) for x in lines[0].split(" ")[1:]]
        map_titles = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
                      "light-to-temperature", "temperature-to-humidity", "humidity-to-location",]
        seed_data = []
        source = ""
        destination = ""
        for line in lines[1:]:
            for title in map_titles:
                if title in line:
                    title_split = title.split("-")
                    source = title_split[0]
                    destination = title_split[2]
                    break
            line_split = line.split(" ")
            if len(line_split) == 3:
                src_start = int(line_split[1])
                dst_start = int(line_split[0])
                rng = int(line_split[2])
                item = AlmanacItem(
                    source, destination, src_start, src_start + rng, dst_start, dst_start+rng)
                seed_data.append(item)
        self.seeds = seeds
        self.almanac = seed_data

    def transform_almanac(self, src, id) -> (str, int):
        if (src == "location"):
            return ("done", id)
        for item in self.almanac:
            if src == item.source and id >= item.source_start and id < item.source_end:
                diff = id - item.source_start
                return (item.desination, item.destination_start + diff)
        return (self.src_dst_list[src], id)

    def solve(self, id: int) -> int:
        src = "seed"
        while (src != "done"):
            src, id = self.transform_almanac(src, id)
        return id

    def solvePart1(self) -> int:
        results = []
        for s in tqdm(self.seeds):
            results.append(self.solve(s))
        return min(results)

    def solvePart2(self) -> int:
        total = 0
        for i, s in enumerate(self.seeds):
            if i % 2 == 1:
                total += s
        seedsIter = iterSeeds(self.seeds)
        current_best = 9999999999
        try:
            cnt = 0
            while (True):
                if(cnt % 100000 == 0):
                    print(cnt, "/", total)
                s = next(seedsIter)
                loc = self.solve(s)
                if loc < current_best:
                    current_best = loc
                cnt += 1
        except:
            pass
        return current_best


def iterSeeds(seeds):
    base = 0
    cnt = 0
    for i in range(len(seeds)):
        if i % 2 == 0:
            base = seeds[i]
        if i % 2 == 1:
            cnt = seeds[i]
            for c in range(base, base + cnt):
                yield c
    raise StopIteration


if __name__ == '__main__':
    d = Day1()
    d.parse(load_input(5, 1))
    print("### PART 1 ####")
    print(d.solvePart1())
    print("### PART 2 ###")
    print(d.solvePart2())
