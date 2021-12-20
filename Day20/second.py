from collections import defaultdict
import sys


def main():
    with open(sys.argv[1], "r") as f:
        pattern, image = f.read().split("\n\n")

    print(pattern)
    summ = 0
    for pat in pattern:
        summ += len(pat.strip())
    print(summ)
    pattern = "".join([line.strip() for line in pattern.splitlines()])
    mapp = defaultdict(lambda: 0)
    print("pattern", pattern, len(pattern))
    print(image)
    image = image.splitlines()
    print("image", image)

    for i, line in enumerate(image):
        line = line.strip()
        for j, c in enumerate(line):
            mapp[(i, j)] = 0 if c == "." else 1
    delta = 60
    for i in range(-delta, len(image) + delta):
        for j in range(-delta, len(image[0]) + delta):
            print("." if mapp[(i, j)] == 0 else "#", end="")
        print()

    for itr in range(50):
        if itr % 2 == 1:
            new_mapp = defaultdict(lambda: 0)
        else:
            new_mapp = defaultdict(lambda: 1)
        for i in range(-delta, len(image) + delta):
            for j in range(-delta, len(image[0]) + delta):
                num = 0
                for idx_i in range(i - 1, i + 2, 1):
                    for idx_j in range(j - 1, j + 2, 1):
                        num = num * 2 + mapp[(idx_i, idx_j)]
                new_mapp[(i, j)] = 1 if pattern[num] == "#" else 0
        mapp = new_mapp
        count = 0
        for i in range(-delta, len(image) + delta):
            for j in range(-delta, len(image[0]) + delta):
                # print("." if mapp[(i, j)] == 0 else "#", end="")
                count += mapp[(i, j)]
            # print()
        print(count)


if __name__ == "__main__":
    main()
