from common import read_input, write_output


def parse_input(inp: list[str]):
    [_, seeds] = inp[0].split(":")
    seeds = [int(s) for s in seeds.strip().split()]

    maps = []
    current = {}
    for i in range(2, len(inp)):
        if len(inp[i]) == 0:
            # empty line, new map
            maps.append(current)
            current = {}
        elif "map" in inp[i]:
            # map description
            [source, dest] = inp[i][:-5].split("-to-")
            current = {"source": source, "dest": dest, "ranges": []}
        else:
            # map contents
            [dest_start, src_start, rg] = [int(n) for n in inp[i].split()]
            current["ranges"].append((dest_start, src_start, rg))

    # add last
    if current != {}:
        maps.append(current)

    return (seeds, maps)


def part1(inp: list[str]):
    seeds, maps = parse_input(inp)

    locations = []
    for seed in seeds:
        out = seed
        for i in range(len(maps)):
            cmap = maps[i]

            for j in range(len(cmap["ranges"])):
                dest_start, src_start, rg = cmap["ranges"][j]
                if out in range(src_start, src_start + rg):
                    out = dest_start + out - src_start
                    break
        locations.append(out)
    return min(locations)


def part2(inp: list[str]):
    return 0


if __name__ == "__main__":
    inp = read_input("../inputs/day05.txt")

    p1 = part1(inp)
    p2 = part2(inp)
    write_output("../outputs/day05.txt", p1, p2)
