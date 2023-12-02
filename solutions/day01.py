from common import read_input, write_output


def part1(inp: list[str]):
    digits = list(map(lambda s: list(filter(lambda c: c.isdigit(), s)), inp))
    result = sum(
        map(lambda arr: 10 * int(arr[0]) + int(arr[-1]) if len(arr) > 0 else 0, digits)
    )
    return result


def part2(inp: list[str]):
    words = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(len(inp)):
        for j in range(len(words)):
            inp[i] = inp[i].replace(words[j], f"{words[j]}{digits[j]}{words[j]}")

    return part1(inp)


if __name__ == "__main__":
    inp = read_input("../inputs/day01.txt")

    p1 = part1(inp)
    p2 = part2(inp)
    write_output("../outputs/day01.txt", p1, p2)
