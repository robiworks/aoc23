#!/bin/bash

DAY_NUMBER="$(printf '%02d' $1)"

TEMPLATE="$(cat << EOF
from common import read_input, write_output


def part1(inp: list[str]):
    return 0


def part2(inp: list[str]):
    return 0


if __name__ == "__main__":
    inp = read_input("../inputs/day${DAY_NUMBER}.txt")

    p1 = part1(inp)
    p2 = part2(inp)
    write_output("../outputs/day${DAY_NUMBER}.txt", p1, p2)
EOF
)"

SOL_PATH="$(dirname $(realpath $0))/solutions/day${DAY_NUMBER}.py"
INP_PATH="$(dirname $(realpath $0))/inputs/day${DAY_NUMBER}.txt"

echo "$TEMPLATE" > $SOL_PATH
touch "$INP_PATH"
