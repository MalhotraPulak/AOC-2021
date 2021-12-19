from collections import defaultdict
import sys
import pprint
from itertools import permutations


def subt(pt1, pt2):
    return pt1[0] - pt2[0], pt1[1] - pt2[1], pt1[2] - pt2[2]


def add(pt1, pt2):
    return pt1[0] + pt2[0], pt1[1] + pt2[1], pt1[2] + pt2[2]


def rotate(pt, permut):
    return pt[permut[0]], pt[permut[1]], pt[permut[2]]


def change_sign(pt, sign):
    return pt[0] * sign[0], pt[1] * sign[1], pt[2] * sign[2]


def get_relative_dist(pts1, pts2):
    max_len = 0
    pts_old = set(pts1)
    signs = [
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
    ]

    for pt in pts1:
        for pt2 in pts2:
            for permut in permutations((0, 1, 2)):
                for sign in signs:
                    pt2_rotated = rotate(pt2, permut)
                    pt2_signed = change_sign(pt2_rotated, sign)
                    diff = subt(pt, pt2_signed)

                    new_pts = []
                    for pt3 in pts2:
                        new_pts.append(
                            add(change_sign(rotate(pt3, permut), sign), diff)
                        )

                    new_pts = set(new_pts)
                    common = new_pts.intersection(pts_old)

                    if len(common) > max_len:
                        max_len = len(common)
                        if max_len >= 12:
                            pprint.pprint(common)
                            print("Returning", diff, permut, sign)
                            return diff, permut, sign

    return None


def transform(pts, diff, permut, sign):
    ans = []
    for pt in pts:
        ans.append(add(change_sign(rotate(pt, permut), sign), diff))
    return ans


def main():
    with open(sys.argv[1], "r") as f:
        text = f.read()

    scanner = text.split("\n\n")

    pts = []
    for line in scanner:
        inputs = line.split("\n")
        st_pts = []
        for st in inputs[1:]:
            if st == "":
                continue
            x, y, z = st.split(",")
            st_pts.append((int(x), int(y), int(z)))
        pts.append(st_pts)

    edge_map = {}
    adj_map = defaultdict(lambda: [])
    for i in range(0, len(pts)):
        for j in range(0, len(pts)):
            if i == j:
                continue
            res = get_relative_dist(pts[i], pts[j])
            if res is not None:
                edge_map[(i, j)] = res
                adj_map[i].append(j)
                print(f"{i} relative to {j} is ", res)

    from collections import deque

    total = set(pts[0])
    for i in range(1, len(pts)):
        q = deque()
        q.append(i)
        visited = set()
        visited.add(i)
        mp = {}
        while q:
            curr = q.popleft()
            if curr == 0:
                dts = [0]
                while curr != i:
                    curr = mp[curr]
                    dts.append(curr)

                from copy import deepcopy

                print("Found a way to reach 0 from", i)
                print(dts)

                ptts = deepcopy(pts[i])

                for j in range(len(dts) - 1, 0, -1):
                    edge = (dts[j - 1], dts[j])
                    diff, permut, sign = edge_map[edge]
                    print("Applied edge", edge)
                    print("Got", diff, permut, sign)

                    ptts = transform(ptts, diff, permut, sign)
                    pprint.pprint(ptts)
                total.update(ptts)
                break

            for x in adj_map[curr]:
                if x in visited:
                    continue
                visited.add(x)
                q.append(x)
                mp[x] = curr

    print("answer is", total)
    print("final answer is", len(total))


if __name__ == "__main__":
    main()
