from typing import Literal

Order = Literal["forwards", "backwards"]


VALUES = [
    "one",
    "1",
    "two",
    "2",
    "three",
    "3",
    "4",
    "four",
    "five",
    "5",
    "6",
    "six",
    "seven",
    "7",
    "8",
    "eight",
    "9",
    "nine",
]

MAP = {word: (index // 2) + 1 for index, word in enumerate(VALUES)}


def _add_to_trie(trie: dict, word: str) -> None:
    current = trie

    for letter in word:
        if next := current.get(letter):
            current = next
            continue

        current[letter] = {}
        current = current[letter]

    current["value"] = MAP[word]


def _build_trie() -> dict:
    trie = {}
    for word in VALUES:
        _add_to_trie(trie, word)
    return trie


def find_last(line: str, trie: dict) -> int:
    num_chars = len(line)
    left = num_chars - 1

    if "value" in trie.get(line[left], {}):
        return int(trie[line[left]]["value"])

    left = left - 1

    while left >= 0:
        while not trie.get(line[left]) and left > 0:
            left -= 1

        try:
            return find_first(line[left:], trie)
        except (ValueError, KeyError):
            left -= 1

    raise ValueError("Couldn't find last in ", line)


def find_first(line: str, trie: dict) -> int:
    left = 0
    right = 1
    num_chars = len(line)

    while left < num_chars:
        while not trie.get(line[left]) and right < num_chars:
            left = right
            right += 1

        current = trie[line[left]]
        if ans := current.get("value"):
            return ans

        if right >= num_chars:
            raise ValueError("Right too large: ", right, line)

        while current.get(line[right]) and right < num_chars:
            current = current[line[right]]
            right += 1

            if ans := current.get("value"):
                return ans

        left += 1
        right = left + 1

    raise ValueError("Couldn't find answer in ", line)


def solve(lines: list[str]) -> None:
    print("Part 2:")
    trie = _build_trie()
    import ipdb; ipdb.set_trace(context=20)

    nums = []
    for line in lines:
        first = find_first(line, trie)
        last = find_last(line, trie)
        nums.append(int(f"{first}{last}"))
    print("Answer: ", sum(nums))
