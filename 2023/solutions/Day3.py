from data_loader import load_input


class Day3():
    part1_example_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
    part1_example_solution = 4361

    part2_example_input = ''''''
    part2_example_solution = 281

    def solvePart1(self, input: str) -> int:
        lines = input.splitlines()

        def is_symbol(c: chr) -> bool:
            return c in '!@#$%^&*()_-+={}[]'

        def find_number(x, y) -> int:
            if not lines[y][x].isdigit():
                return 0
            
            num = int(lines[y][x])
            i = 1
            while x + i < len(lines[y])-1 and lines[y][x+i].isdigit():  # look right
                num = num * 10 + int(lines[y][x+i])
                i += 1

            i = -1
            while x - i < len(lines[y])-1 and lines[y][x+i].isdigit():  # look left
                num = num + 10 * int(lines[y][x+i])
                i -= 1

            return num

        def is_in_range(x, y) -> bool:
            return x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines)

        def find_surrounding_numbers(x, y) -> list:
            dirs = [
                (-1, -1),
                (1, 1),
                (1, 0),
                (1, -1),
                (0, 1),
                (0, -1),
                (-1, 0),
                (-1, 1),
            ]
            nums = []
            for d in dirs:
                off_x = x + d[0]
                off_y = y + d[1]
                if is_in_range(off_x, off_y):
                    nums.append(find_number(off_x, off_y))
            return nums

        overall_sum = 0
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if is_symbol(c):
                    nums = find_surrounding_numbers(x, y)
                    print(nums)
                    s = sum(nums)
                    overall_sum += s
        return overall_sum

    def solvePart2(self, input: str) -> int:
        return 0


if __name__ == '__main__':
    d = Day3()
    print("### Part 1 ###")
    print(d.solvePart1(d.part1_example_input) == d.part1_example_solution)
    print(d.solvePart1(load_input(day=3)))
   #  print("### Part 2 ###")
   #  print(d.solvePart2(d.part2_example_input) == d.part2_example_solution)
   #  print(d.solvePart2(load_input(day=1, part=2)))
