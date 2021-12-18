import sys


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    start = lines[0].strip()
    mapp = {}
    print(lines)
    for line in lines[2:]:
        left, right = line.split("->")
        left = left.strip()
        right = right.strip()
        first = left[0]
        mapp[left] = first + right

    print(mapp)

    for _ in range(10):
        new_str = []
        for i, _ in enumerate(start):
            if i == len(start) - 1:
                new_str.append(start[i])
                continue

            key = start[i] + start[i + 1]
            if key in mapp:
                new_str.append(mapp[start[i] + start[i + 1]])
            else:
                new_str.append(start[i])

        start = "".join(new_str)
        print(start)
    from collections import Counter

    D = Counter(start)
    print(D.most_common())


if __name__ == "__main__":
    main()
