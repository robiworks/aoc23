from common import read_input, write_output


def parse_input(inp: list[str]) -> list[tuple[list[int], list[int]]]:
    output = []
    for line in inp:
        [_, nums] = line.split(":")
        [win, min] = nums.split("|")

        winning = sorted([int(w) for w in win.strip().split()])
        mine = sorted([int(m) for m in min.strip().split()])
        output.append((winning, mine))

    return output


def part1(inp: list[str]):
    cards = parse_input(inp)
    result = 0

    for winning, mine in cards:
        matches = len(set(winning) & set(mine))
        result += int(2 ** (matches - 1))

    return result


def part2(inp: list[str]):
    cards = parse_input(inp)
    result = [1] * len(cards)

    for i in range(len(cards)):
        winning, mine = cards[i]
        matches = len(set(winning) & set(mine))

        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            result[j] += result[i]

    return sum(result)


if __name__ == "__main__":
    inp = read_input("../inputs/day04.txt")

    p1 = part1(inp)
    p2 = part2(inp)
    write_output("../outputs/day04.txt", p1, p2)
