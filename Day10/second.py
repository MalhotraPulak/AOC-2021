import sys


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    maps = {"(": 1, "[": 2, "{": 3, "<": 4}
    costs = []

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
                    break
        else:
            cost = 0
            while len(stack) > 0:
                ele = stack.pop()
                cost = cost * 5 + maps[ele]
            costs.append(cost)

    costs.sort()
    print(costs)
    print(costs[len(costs) // 2])


if __name__ == "__main__":
    main()
