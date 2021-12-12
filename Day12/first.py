from collections import defaultdict
import sys
import pprint

count = 0


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    adj = defaultdict(lambda: [])

    for line in lines:
        start, end = line.split("-")
        start = start.strip()
        end = end.strip()
        adj[start].append(end)
        adj[end].append(start)

    def dfs(node, path):

        print(node, path)
        if node == "end":
            global count
            count += 1
            return

        path.append(node)

        for child in adj[node]:
            if child.isupper() or child not in path:
                dfs(child, path.copy())

    global count
    count = 0
    dfs("start", [])

    print(count)


if __name__ == "__main__":
    main()
