import argparse
from parts import part_1, part_2


def get_file(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--part")
    parser.add_argument("--puzzle", action="store_true")

    args = parser.parse_args()
    part = int(args.part)

    if args.puzzle:
        filename = "inputs/puzzle.txt"
    else:
        filename = f"inputs/test{part}.txt"
    lines = get_file(filename)

    if part == 1:
        part_1.solve(lines)
    # elif part == 2:
    else:
        part_2.solve(lines)


if __name__ == "__main__":
    main()
