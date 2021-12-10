import sys
from operator import add


dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


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
    rows = len(nums)
    cols = len(nums[0])
    dp = {}

    def end(p, ending_pts):

        if small_neighbour(p) == 0:
            ending_pts.append(p)
            return

        curr_val = nums[p[0]][p[1]]

        for a_dir in dirs:
            new_pos_x = p[0] + a_dir[0]
            new_pos_y = p[1] + a_dir[1]

            if (
                valid((new_pos_x, new_pos_y))
                and nums[new_pos_x][new_pos_y] < curr_val
            ):
                end((new_pos_x, new_pos_y), ending_pts)

    def all_dfs(p):
        ans = 0
        for i, line in enumerate(nums):
            for j, c in enumerate(line):
                if c == 9:
                    continue
                ending_pts = []
                end((i, j), ending_pts)
                if ending_pts == [p]:
                    ans += 1
        return ans

    def valid(p):
        if 0 <= p[0] < rows and 0 <= p[1] < cols:
            return True
        return False

    def small_neighbour(p):
        count = 0
        for a_dir in dirs:
            new_pos = (p[0] + a_dir[0], p[1] + a_dir[1])
            if (
                valid(new_pos)
                and nums[new_pos[0]][new_pos[1]] < nums[p[0]][p[1]]
            ):
                count += 1
        return count

    ans = []
    for i, line in enumerate(nums):
        for j, c in enumerate(line):
            pos = (i, j)
            flag = True
            for a_dir in dirs:
                new_pos = (pos[0] + a_dir[0], pos[1] + a_dir[1])
                if valid(new_pos) and nums[new_pos[0]][new_pos[1]] <= c:
                    flag = False
                    break

            if flag:
                ans.append(all_dfs(pos))
                print(
                    "Got ans =", ans[-1], "for position", pos, "with value", c
                )

    print(sorted(ans, reverse=True)[:3])


if __name__ == "__main__":
    main()
