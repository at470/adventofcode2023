from __future__ import annotations

import re
import abc

import dataclasses as dc


@dc.dataclass
class HasColors(abc.ABC):
    red: int
    green: int
    blue: int


@dc.dataclass
class Cubes(HasColors):
    def game_valid(self, game: Game) -> bool:
        for color in ["red", "blue", "green"]:
            available = getattr(self, color)
            drawn = getattr(game, color)

            if available < drawn:
                return False
        return True


@dc.dataclass
class Game(HasColors):
    id: int
    red: int
    green: int
    blue: int

    @classmethod
    def from_line(cls, line: str) -> Game:
        game, cubes = line.split(":")
        game_id = re.sub(r"[A-Za-z\ ]+", "", game)

        maxes = {"red": 0, "blue": 0, "green": 0}
        for round in cubes.split(";"):
            round = round.strip()
            for draw in round.split(","):
                draw = draw.strip()
                split_draw = draw.split(" ")
                num = split_draw[0]
                color = split_draw[1]
                maxes[color] = max(int(num), maxes[color])

        return cls(
            id=int(game_id), red=maxes["red"], green=maxes["green"], blue=maxes["blue"]
        )


def parse(lines: list[str]) -> list[Game]:
    return [Game.from_line(l) for l in lines]


def solve(lines: list[str]) -> None:
    print("Part 1:")
    games = parse(lines)
    requirements = Cubes(red=12, green=13, blue=14)

    total = 0
    for game in games:
        if not requirements.game_valid(game):
            continue
        total += game.id

    print("Answer: ", total)
