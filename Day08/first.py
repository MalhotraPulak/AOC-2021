import sys


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    lines = [line.split("|") for line in lines]

    ans = 0
    for f, s in lines:
        outputs = s.strip().split()
        ans += len([out for out in outputs if len(out) in [2, 4, 3, 7]])

    print(ans)


if __name__ == "__main__":
    main()
