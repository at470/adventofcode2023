import argparse

from parts import one, two


def get_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--part")
    parser.add_argument("--puzzle", action="store_true")

    args = parser.parse_args()

    if args.puzzle:
        filename = "inputs/puzzle.txt"
    else:
        filename = "inputs/test.txt"

    lines = get_file(filename)

    if int(args.part) == 1:
        one.solve(lines)
    else:
        two.solve(lines)


if __name__ == "__main__":
    main()
