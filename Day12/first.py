from collections import defaultdict
import sys
from copy import deepcopy

count = 0


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    adj = defaultdict(lambda: [])

    lowers = []
    for line in lines:
        start, end = line.split("-")
        start = start.strip()
        end = end.strip()
        adj[start].append(end)
        adj[end].append(start)
        if start.islower():
            lowers.append(start)
        if end.islower():
            lowers.append(end)

    def dfs(node, path, powerup):

        if node == "end":
            global count
            count += 1
            return

        path[node] += 1

        for child in adj[node]:
            if child == "start":
                continue

            if child.isupper() or path[child] == 0:
                dfs(child, deepcopy(path), powerup)
            elif path[child] == 1 and powerup:
                dfs(child, deepcopy(path), False)

    global count
    count = 0
    p = defaultdict(lambda: 0)
    dfs("start", p, True)

    print(count)


if __name__ == "__main__":
    main()
