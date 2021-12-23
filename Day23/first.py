from copy import deepcopy
import functools

# State: (A, A2, B, B2, C, C3, D, D2)
"""

#01234567891#
#...........#
###D#B#D#B###
  #C#A#A#C#
  #########

11, 12 AA
13, 14 BB
15, 16 CC
17, 18 DD

"""
## 11, 12 AA
## 13, 14 BB
## 15, 16 CC
## 17, 18 DD
def valid(st):
    if (
        11 <= st[0] <= 12
        and 11 <= st[1] <= 12
        and 13 <= st[2] <= 14
        and 13 <= st[3] <= 14
        and 15 <= st[4] <= 16
        and 15 <= st[5] <= 16
        and 17 <= st[6] <= 18
        and 17 <= st[7] <= 18
    ):
        return True
    return False


cost = {
    0: 1,
    1: 1,
    2: 10,
    3: 10,
    4: 100,
    5: 100,
    6: 1000,
    7: 1000,
}

hallway_entrance = {
    11: 2,
    12: 2,
    13: 4,
    14: 4,
    15: 6,
    16: 6,
    17: 8,
    18: 8,
}


def get_symbol(idx):
    if idx in [0, 1]:
        return "A"
    if idx in [2, 3]:
        return "B"
    if idx in [4, 5]:
        return "C"
    if idx in [6, 7]:
        return "D"
    return "."


def print_state(st):
    strr = str("." * 11)
    for idx, s in enumerate(st):
        if s >= 11:
            continue
        strr = list(strr)
        if idx in [0, 1]:
            strr[s] = "A"
        if idx in [2, 3]:
            strr[s] = "B"
        if idx in [4, 5]:
            strr[s] = "C"
        if idx in [6, 7]:
            strr[s] = "D"
        strr = "".join(strr)

    print(strr)
    from collections import defaultdict

    mapp = defaultdict(lambda: 9)
    for idx, s in enumerate(st):
        mapp[s] = idx
    print(
        f"##{get_symbol(mapp[11])}#{get_symbol(mapp[13])}#{get_symbol(mapp[15])}#{get_symbol(mapp[17])}##"
    )
    print(
        f"##{get_symbol(mapp[12])}#{get_symbol(mapp[14])}#{get_symbol(mapp[16])}#{get_symbol(mapp[18])}##"
    )


def is_hallway(pos):
    if pos > 10:
        return False
    return True


@functools.lru_cache(maxsize=None)
def recur(st):
    if valid(st):
        return 0

    # do all possible movements
    cc = int(1e5)
    for i in range(8):
        # dont modify st
        # if current position is valid then skip
        loc = i
        if loc % 2 == 1:
            loc -= 1

        if st[i] == loc + 12:
            continue

        if i % 2 == 1:
            other = i - 1
        else:
            other = i + 1

        if st[other] == loc + 12 and st[i] == loc + 11:
            continue

        current = st[i]
        if not is_hallway(current):
            hallway_pos = [0, 1, 3, 5, 7, 9, 10]
            entrance = hallway_entrance[current]
            for hallway_dest in hallway_pos:
                state = list(deepcopy(st))
                mini = min(hallway_dest, entrance)
                maxi = max(hallway_dest, entrance)
                steps = [i for i in range(mini, maxi + 1)]
                if current % 2 == 0:
                    steps.append(current - 1)

                possible = True
                for step in steps:
                    if step in state:
                        possible = False
                if not possible:
                    continue
                fee = cost[i] * len(steps)
                state[i] = hallway_dest
                # breakpoint()
                cc = min(cc, fee + recur(tuple(state)))
        else:  ## in hallway
            # 0, 1 => 11, 12
            loc = i
            if loc % 2 == 1:
                loc -= 1
            dests = [loc + 11, loc + 12]

            for idx, dest in enumerate(dests):
                # the dests should be empty
                if dest in st:
                    # if any pawn at the destination then continue
                    continue

                if idx == 0:
                    # check if last is correctly filled or not
                    last = loc + 12
                    other = i
                    if i % 2 == 1:
                        other = i - 1
                    else:
                        other = i + 1
                    if st[other] != last:
                        continue

                entrance = hallway_entrance[dest]
                current = st[i] - 1 if entrance < st[i] else st[i] + 1
                mini = min(current, entrance)
                maxi = max(current, entrance)
                steps = [i for i in range(mini, maxi + 1)]
                if dest % 2 == 0:
                    steps.append(dest - 1)
                steps.append(dest)
                possible = True
                for step in steps:
                    if step in st:
                        possible = False
                if not possible:
                    continue
                fee = cost[i] * len(steps)
                state = list(deepcopy(st))
                state[i] = dest
                # breakpoint()
                cc = min(cc, fee + recur(tuple(state)))
    return cc


def main():
    """
    errors
    (12, 18, 0, 1, 15, 16, 14, 17)
    """
    """

    #01234567891#
    #...........#
    ###D#B#D#B###
      #C#A#A#C#
      #########

    11, 12 AA
    13, 14 BB
    15, 16 CC
    17, 18 DD

    """
    state_ques = (14, 16, 13, 17, 12, 18, 11, 15)
    # state_sample = (12, 18, 11, 15, 13, 16, 14, 17)
    ans = recur(state_ques)
    print(ans)


if __name__ == "__main__":
    main()
