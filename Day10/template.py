import sys


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    illegal = {}
    for line in lines:
        line = line.strip()
        stack = []

        for c in line:
            if c in ["[", "{", "(", "<"]:
                stack.append(c)
            else:
                ele = stack.pop()
                if (
                    (ele == "[" and c == "]")
                    or (ele == "{" and c == "}")
                    or (ele == "<" and c == ">")
                    or (ele == "(" and c == ")")
                ):
                    continue
                else:
                    illegal.setdefault(c, 0)
                    illegal[c] += 1
                    break
    print(illegal)
    print(
        illegal[")"] * 3
        + illegal["]"] * 57
        + illegal["}"] * 1197
        + illegal[">"] * 25137
    )


if __name__ == "__main__":
    main()
