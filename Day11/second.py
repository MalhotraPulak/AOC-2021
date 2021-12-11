import sys
import collections


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    grid = collections.defaultdict(lambda: -50000000)

    for x, line in enumerate(lines):
        line = line.strip()
        for y, c in enumerate(line):
            grid[(x, y)] = int(c)

    def neigh(p):
        return [
            (p[0] + 1, p[1]),
            (p[0] + 1, p[1] + 1),
            (p[0] + 1, p[1] - 1),
            (p[0] - 1, p[1]),
            (p[0] - 1, p[1] + 1),
            (p[0] - 1, p[1] - 1),
            (p[0], p[1] + 1),
            (p[0], p[1] - 1),
        ]

    STEP = 10000
    flash = 0
    step = 0
    for step in range(STEP):
        for k in grid:
            grid[k] += 1

        to_flash = collections.deque([k for k, v in grid.items() if v > 9])
        flashed = set(to_flash)

        while len(to_flash) > 0:
            ele = to_flash.popleft()
            flash += 1
            for n in neigh(ele):
                if n not in flashed:
                    grid[n] += 1
                    if grid[n] > 9:
                        flashed.add(n)
                        to_flash.append(n)

        if len(flashed) == 100:
            break

        for ele in flashed:
            grid[ele] = 0

    print(f"step={step + 1}")
    print(f"{flash=}")


if __name__ == "__main__":
    main()
