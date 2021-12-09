import sys
from operator import add


def main():
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    nums = []
    for line in lines:
        line = line.strip()
        num = []
        for c in line:
            num.append(int(c))
        nums.append(num)

    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    rows = len(nums)
    cols = len(nums[0])

    def valid(p):
        if 0 <= p[0] < rows and 0 <= p[1] < cols:
            return True
        return False

    ans = 0
    for i, line in enumerate(nums):
        for j, c in enumerate(line):
            pos = [i, j]
            flag = True
            for a_dir in dirs:
                new_pos = list(map(add, pos, a_dir))
                if valid(new_pos) and nums[new_pos[0]][new_pos[1]] <= c:
                    flag = False
                    break

            if flag:
                ans += c + 1

    print(ans)


if __name__ == "__main__":
    main()
