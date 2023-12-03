from common import read_input, write_output


def parse_input(inp: list[str]):
    # Should return a list of symbol coordinates and number coordinates
    symbols = []
    numbers = []

    for i in range(len(inp)):
        number = None

        for j in range(len(inp[i])):
            if inp[i][j].isdigit():
                if number != None:
                    number = 10 * number + int(inp[i][j])
                else:
                    number = int(inp[i][j])
            elif inp[i][j] != ".":
                symbols.append((i, j, inp[i][j]))
                if number != None:
                    l = len(str(number))
                    numbers.append(
                        (i, [j - offset for offset in range(1, l + 1)], number)
                    )
                number = None
            else:
                if number != None:
                    l = len(str(number))
                    numbers.append(
                        (i, [j - offset for offset in range(1, l + 1)], number)
                    )
                number = None

        if number != None:
            l = len(str(number))
            numbers.append((i, [j - offset for offset in range(1, l + 1)], number))

    return symbols, numbers


def part1(inp: list[str]):
    symbols, numbers = parse_input(inp)

    result = 0
    for yn, xn, num in numbers:
        for ys, xs, _ in symbols:
            # horizontal
            if ys == yn and (xs - 1 in xn or xs + 1 in xn):
                result += num
                break
            # vertical
            if xs in xn and (ys - 1 == yn or ys + 1 == yn):
                result += num
                break
            # diagonal
            if (ys - 1 == yn or ys + 1 == yn) and (xs - 1 in xn or xs + 1 in xn):
                result += num
                break

    return result


def part2(inp: list[str]):
    symbols, numbers = parse_input(inp)

    result = 0
    for ys, xs, sym in symbols:
        if sym == "*":
            matches = [
                (yn, xn, num)
                for (yn, xn, num) in numbers
                if (ys == yn and (xs - 1 in xn or xs + 1 in xn))
                or (xs in xn and (ys - 1 == yn or ys + 1 == yn))
                or ((ys - 1 == yn or ys + 1 == yn) and (xs - 1 in xn or xs + 1 in xn))
            ]

            if len(matches) == 2:
                result += matches[0][2] * matches[1][2]

    return result


if __name__ == "__main__":
    inp = read_input("../inputs/day03.txt")

    p1 = part1(inp)
    p2 = part2(inp)
    write_output("../outputs/day03.txt", p1, p2)
