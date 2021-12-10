import sys
import collections


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    grid = collections.defaultdict(lambda: 9)

    rows = len(lines)
    cols = len(lines[0].strip())
    for x, line in enumerate(lines):
        line = line.strip()
        for y, c in enumerate(line):
            grid[(x, y)] = int(c)

    def neigh(x, y):
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def valid(p):
        return 0 <= p[0] < rows and 0 <= p[1] < cols

    def get_size(x, y):
        q = [(x, y)]
        size = 0
        visited = set()
        visited.add(q[0])
        while len(q) > 0:
            x, y = q.pop()
            size += 1
            for neighbour in neigh(x, y):
                if (
                    valid(neighbour)
                    and grid[neighbour] != 9
                    and neighbour not in visited
                ):
                    q.append(neighbour)
                    visited.add(neighbour)
        return size

    lowers = []
    for i in range(rows):
        for j in range(cols):
            val = grid[(i, j)]
            higher = 0
            for neighbour in neigh(i, j):
                higher += 1 if grid[neighbour] > val else 0
            if higher == 4:
                lowers.append(get_size(i, j))

    lowers.sort()
    print(lowers[-3] * lowers[-2] * lowers[-1])


if __name__ == "__main__":
    main()
