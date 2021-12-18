from collections import defaultdict
import sys
from heapq import heappop
from heapq import heappush


def n(x, y):
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    h_x = len(lines)
    w = len(lines[0].strip())

    print(lines, h_x, w)

    def valid(x, y):
        return 0 <= x < h_x and 0 <= y < w

    dist = defaultdict(lambda: int(1e9))
    dist[(0, 0)] = 0

    h = []
    heappush(h, (dist[(0, 0)], (0, 0)))

    while h:
        d, node = heappop(h)

        if d != dist[node]:
            continue

        for neigh in n(*node):
            if not valid(*neigh):
                continue

            weight = int(lines[neigh[0]][neigh[1]])

            if dist[neigh] > dist[node] + weight:
                dist[neigh] = dist[node] + weight
                heappush(h, (dist[neigh], neigh))

    print(dist[(h_x - 1, w - 1)])


if __name__ == "__main__":
    main()
