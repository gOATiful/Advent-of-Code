from dataclasses import dataclass
from tqdm import tqdm
from data_loader import load_input


@dataclass
class Race:
    time: int
    distance: int


class Day6():
    races: list[Race]

    def parse(self, input: str):
        lines = input.splitlines()
        times = [int(x) for x in lines[0].split(" ") if x.isdecimal()]
        distances = [int(x) for x in lines[1].split(" ") if x.isdecimal()]
        races = [Race(t, distances[i]) for i, t in enumerate(times)]
        self.races = races

    def parse_part2(self, input: str):
        lines = input.splitlines()
        time = int("".join(lines[0].replace("Time:", "").split(" ")))
        distance = int("".join(lines[1].replace("Distance:", "").split(" ")))
        self.races = [Race(time, distance)]
        


    def solve_part1(self):
        solution = 1
        for race in self.races:
            cnt = 0
            for trigger_time in tqdm(range(race.time)):
                race_time = race.time - trigger_time
                speed = trigger_time
                distance_traveled = speed * race_time
                if distance_traveled > race.distance:
                    cnt += 1
            solution *= cnt
        return solution

    def solve_part2(self):
        return self.solve_part1()

    def solve_part1_fast(self):
        for race in self.races:
            trigger_time = race.time / 2
            max_dist = self.calc_distance(trigger_time, race.time)        

        
    def calc_distance(self, trigger_time: int, race_time: int) -> int:
        travel_time = race_time - trigger_time
        speed = trigger_time
        return speed * travel_time

if __name__ == '__main__':
    d = Day6()
    print("### PART 1 ####")
    d.parse(load_input(6,1))
    print(d.solve_part1())
    print("### PART 2 ####")
    d.parse_part2(load_input(6,1))
    print(d.solve_part2())
