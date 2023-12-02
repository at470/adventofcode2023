from __future__ import annotations

from . import one


def get_min_cubes_power(game: one.Game) -> int:
    return game.red * game.green * game.blue


def solve(lines: list[str]) -> None:
    print("Part 2:")
    games = one.parse(lines)
    print("Answer: ", sum([get_min_cubes_power(game) for game in games]))
