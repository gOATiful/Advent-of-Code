input_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

input_data2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

def load_input(input_file_path = "day9/input.txt"):
  with open(input_file_path, "r") as input_file:
    return input_file.read()

# input_data = load_input()

moves= {
  "R": (1, 0),
  "L": (-1,0),
  "U": (0, 1),
  "D": (0, -1),
}

class Tail():
  def __init__(self, x, y, name, next):
      self.x = x
      self.y = y
      self.name = name
      self.tail = next
      self.visited = set()

  def follow(self, head_x, head_y):
    dir_x = head_x - self.x
    dir_y = head_y - self.y
    if dir_x > 1:
      self.x += 1
      self.y = head_y
    elif dir_x < -1:
      self.x -= 1
      self.y = head_y
    elif dir_y > 1:
      self.y += 1
      self.x = head_x
    elif dir_y < -1:
      self.y -= 1
      self.x = head_x
    # notify next tail pice about new position
    if not self.tail is None:
      self.tail.follow(self.x, self.y)
    self.visited.add((self.x, self.y))    

  def visualize(self, board):
    if not self.tail is None:
      self.tail.visualize(board)
    board[self.y][self.x] = self.name
    

class Head():
  def __init__(self, x, y, tail):
    self.x = x
    self.y = y
    self.tail = tail

  def move(self, dir):
    self.x += dir[0]
    self.y += dir[1]
    self.tail.follow(self.x, self.y)

  def visualize(self, board):
    if not self.tail is None:
      self.tail.visualize(board)
    board[self.y][self.x] = "H"

def visualize(head):
  max_x = max(head.x+1, 10)
  max_y = max(head.y+1, 10)
  board = []
  for _ in range(max(5, max_y)):
    row = []
    for _ in range(max(6, max_x)):
      row.append(".")
    board.append(row)

  board[0][0] = "s" # add starting position

  head.visualize(board)

  board.reverse()
  for row in board:
    print(" ".join(row))
  print()

def move_steps(steps: str, head: Head):
  steps_split = steps.split(" ")
  direction = steps_split[0]
  amount = int(steps_split[1])

  print("== {} {:2} ==".format(direction, amount))
  for _ in range(amount):
    head.move(moves[direction])
    visualize(head)

tail = Tail(0,0,"T", None)
head = Head(0,0, tail)

print("== Start ==")
visualize(head)

for row in input_data.splitlines():
  move_steps(row, head)

print("Answer1: {}".format(len(head.tail.visited)))


tail9 = Tail(0,0, "9", None)
tail8 = Tail(0,0, "8", tail9)
tail7 = Tail(0,0, "7", tail8)
tail6 = Tail(0,0, "6", tail7)
tail5 = Tail(0,0, "5", tail6)
tail4 = Tail(0,0, "4", tail5)
tail3 = Tail(0,0, "3", tail4)
tail2 = Tail(0,0, "2", tail3)
tail1 = Tail(0,0, "1", tail2)
head = Head(0,0,tail1)

print("== Start ==")
visualize(head)
# for row in input_data2.splitlines():
move_steps("R 4", head)
move_steps("U 8", head)
