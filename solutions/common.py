def read_input(path: str):
    with open(path) as f:
        lines = f.readlines()
        return [l.strip() for l in lines]


def write_output(path: str, part1: str | int, part2: str | int):
    output = [
        "---- Part 1 ----\n",
        f"{str(part1)}\n",
        "\n",
        "---- Part 2 ----\n",
        f"{str(part2)}\n",
    ]
    with open(path, "w") as f:
        f.writelines(output)

    print(part1, part2)
