import sys
from collections import Counter


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    start = lines[0].strip()
    mapp = {}

    for line in lines[2:]:
        left, right = line.split("->")
        left = left.strip()
        right = right.strip()
        first = left[0]
        second = left[1]
        mapp[left] = (first + right, right + second)

    D = Counter()

    for i, _ in enumerate(start):
        if i == len(start) - 1:
            D[start[i]] += 1
            continue
        l_c = start[i]
        r_c = start[i + 1]
        D[l_c + r_c] += 1

    print(D)

    for _ in range(40):
        E = Counter()

        for key in D:
            if key in mapp:
                E[mapp[key][0]] += D[key]
                E[mapp[key][1]] += D[key]
            else:
                E[key] = D[key]

        D = E

    chars = Counter("".join(D.keys()))

    ans = Counter()
    for char in chars:
        for key in D:
            if key == char + char:
                ans[char] += D[key] * 2
            elif key == char:
                ans[char] += D[key]
            elif char in key:
                ans[char] += D[key]

    print(ans)

    ans[start[0]] += 1
    ans[start[-1]] += 1

    for char in chars:
        ans[char] = ans[char] // 2

    print(ans)
    max_v = max(ans.values())
    min_v = min(ans.values())
    print(max_v - min_v)


if __name__ == "__main__":
    main()
