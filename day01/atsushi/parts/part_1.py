import re


def solve(lines: list[str]) -> None:
    print("Part 1:")
    nums = [_parse(line) for line in lines]
    print("Answer: ", sum(nums))


def _parse(line: str) -> int:
    """
    Part 1
    """
    match = re.sub(r"[A-Za-z]+", "", line)
    return int(f"{match[0]}{match[-1]}")
