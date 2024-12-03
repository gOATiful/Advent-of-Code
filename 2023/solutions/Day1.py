from data_loader import load_input


class Day1():
    part1_example_input = '''1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet'''
    part1_example_solution = 142

    part2_example_input = '''two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen'''
    part2_example_solution = 281

    def solvePart1(self, input: str) -> int:
        res_list = []
        for l in input.splitlines():
            c_line = []
            for c in l:
                if c.isdigit():
                    c_line.append(int(c))
            if len(c_line) > 1:
                res = c_line[0] * 10 + c_line[-1]
            else:
                res = c_line[0] * 10 + c_line[0]
            res_list.append(res)

        return sum(res_list)

    def solvePart2(self, input: str) -> int:
        number_map = {"one": "1", "two": "2", "three": "3", "four": "4",
                      "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        for k, v in number_map.items():
            input = input.replace(k, k[0] + v + k[-1])

        return self.solvePart1(input)


if __name__ == '__main__':
    d = Day1()
    print("### Part 1 ###")
    print(d.solvePart1(d.part1_example_input) == d.part1_example_solution)
    print(d.solvePart1(load_input(day=1)))
    print("### Part 2 ###")
    print(d.solvePart2(d.part2_example_input) == d.part2_example_solution)
    print(d.solvePart2(load_input(day=1, part=2)))
