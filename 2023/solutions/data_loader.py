INPUT_DIR = "inputs"


def load_input(day: int, part: int = 1) -> str:
    with open(f"{INPUT_DIR}/Day{day}_{part}.txt") as infile:
        return infile.read()
