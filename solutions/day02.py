from common import read_input, write_output


def get_color_dict(balls: list[str]):
    r, g, b = 0, 0, 0

    for ball in balls:
        ball = ball.strip()

        if ball.endswith("red"):
            r = int(ball[: ball.index("red") - 1])
        elif ball.endswith("blue"):
            b = int(ball[: ball.index("blue") - 1])
        elif ball.endswith("green"):
            g = int(ball[: ball.index("green") - 1])

    return {"r": r, "g": g, "b": b}


def parse_input(inp: list[str]) -> dict[int, list[dict[str, int]]]:
    dct = {}
    for line in inp:
        [game, lst] = line.split(":")
        game_id = int(game[5:])

        moves = lst.split(";")
        color_dicts = []
        for move in moves:
            balls = move.split(",")
            colors = get_color_dict(balls)
            color_dicts.append(colors)

        dct[game_id] = color_dicts

    return dct


def part1(inp: list[str], r: int, g: int, b: int):
    result = 0
    parsed = parse_input(inp)

    for gid, v in parsed.items():
        result += gid

        for d in v:
            if d["r"] > r or d["g"] > g or d["b"] > b:
                result -= gid
                break

    return result


def part2(inp: list[str]):
    result = 0
    parsed = parse_input(inp)

    for _, v in parsed.items():
        min_r = max([g["r"] for g in v])
        min_g = max([g["g"] for g in v])
        min_b = max([g["b"] for g in v])

        result += min_r * min_g * min_b

    return result


if __name__ == "__main__":
    inp = read_input("../inputs/day02.txt")

    p1 = part1(inp, 12, 13, 14)
    p2 = part2(inp)
    write_output("../outputs/day02.txt", p1, p2)
