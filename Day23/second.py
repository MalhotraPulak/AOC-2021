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
    base = 11
    for i, x in enumerate(st):
        for s in x:
            if not base + 4 * i <= s <= base + 4 * (i + 1):
                return False
    return True


cost = {
    0: 1,
    1: 10,
    2: 100,
    3: 1000,
}


def get_hallway_entrance(pos):
    entrances = [2, 4, 6, 8]
    shift = pos - 11
    entrance = entrances[shift // 4]
    return entrance


def get_symbol(idx):
    if idx in [0]:
        return "A"
    if idx in [1]:
        return "B"
    if idx in [2]:
        return "C"
    if idx in [3]:
        return "D"
    return "."


def print_state(st):
    from collections import defaultdict

    mapp = get_state_mapping(st)
    mapp = defaultdict(lambda: 9, mapp)
    stt = ""
    for s in range(11):
        stt += f"{get_symbol(mapp[s])}"
    print(stt)
    base = 11
    for i in range(4):
        print(
            f"##{get_symbol(mapp[base + i])}#{get_symbol(mapp[base + i + 4])}#{get_symbol(mapp[base + i + 8])}#{get_symbol(mapp[base + i + 12])}##"
        )


def is_hallway(pos):
    if pos > 10:
        return False
    return True


creature_per_type = 4


def get_state_mapping(st):
    dd = {}
    for i, a in enumerate(st):
        for x in a:
            dd[x] = i
    return dd


def current_valid(pos, a_type, st):
    # the creature should be in the ending zone
    if not (
        11 + a_type * creature_per_type
        <= pos
        < 11 + (a_type + 1) * creature_per_type
    ):
        return False

    mapps = get_state_mapping(st)
    for i in range(pos + 1, 11 + creature_per_type * (a_type + 1)):
        if i not in mapps or mapps[i] != a_type:
            return False
    return True


@functools.lru_cache(maxsize=None)
def recur(st):
    if valid(st):
        return 0

    # do all possible movements
    cc = int(1e5)

    all_state_vals = []
    for s in st:
        all_state_vals.extend(s)

    for a_type in range(4):
        for creature in range(4):
            # dont modify st
            # if current position is valid then skip
            current = st[a_type][creature]
            if current_valid(current, a_type, st):
                continue

            if not is_hallway(current):
                hallway_pos = [0, 1, 3, 5, 7, 9, 10]
                entrance = get_hallway_entrance(current)
                for hallway_dest in hallway_pos:
                    mini = min(hallway_dest, entrance)
                    maxi = max(hallway_dest, entrance)
                    steps = [i for i in range(mini, maxi + 1)]
                    shifted = current - 11
                    for i in range(
                        shifted - shifted % creature_per_type, shifted
                    ):
                        steps.append(i + 11)
                    steps.sort()
                    possible = True
                    for step in steps:
                        if step in all_state_vals:
                            possible = False
                    if not possible:
                        continue

                    fee = cost[a_type] * len(steps)
                    state = list(list(x) for x in st)
                    state[a_type][creature] = hallway_dest
                    # breakpoint()
                    cc = min(cc, fee + recur(tuple(tuple(x) for x in state)))
            else:  ## in hallway
                # 0, 1 => 11, 12
                dests = [
                    i
                    for i in range(
                        11 + a_type * creature_per_type,
                        11 + (a_type + 1) * creature_per_type,
                    )
                ]
                for dest in dests:
                    # the dests should be empty
                    if dest in all_state_vals:
                        # if any pawn at the destination then continue
                        continue

                    if not current_valid(dest, a_type, st):
                        continue

                    entrance = get_hallway_entrance(dest)
                    current = current - 1 if entrance < current else current + 1
                    mini = min(current, entrance)
                    maxi = max(current, entrance)
                    steps = [i for i in range(mini, maxi + 1)]
                    shifted = dest - 11
                    for i in range(
                        shifted - shifted % creature_per_type, shifted + 1
                    ):
                        steps.append(i + 11)

                    possible = True
                    for step in steps:
                        if step in all_state_vals:
                            possible = False
                    if not possible:
                        continue

                    fee = cost[a_type] * len(steps)
                    state = list(list(x) for x in st)
                    state[a_type][creature] = dest
                    # breakpoint()
                    cc = min(cc, fee + recur(tuple(tuple(x) for x in state)))
    return cc


def main():
    """
    errors
    (12, 18, 0, 1, 15, 16, 14, 17)
    """
    """
    #############
    #...........#
    ###B#C#B#D###
      #D#C#B#A#
      #D#B#A#C#
      #A#D#C#A#
      #########
    11, 12 AA
    13, 14 BB
    15, 16 CC
    17, 18 DD

    #D#B#D#B#
    #D#C#B#A#
    #D#B#A#C#
    #C#A#A#C#
    """
    # state_ques = (
    #     (14, 21, 24, 26),
    #     (11, 17, 19, 20),
    #     (15, 16, 22, 25),
    #     (12, 13, 18, 23),
    # )
    # state_sample = (12, 18, 11, 15, 13, 16, 14, 17)
    state_ques = (
        (18, 21, 22, 24),
        (15, 17, 20, 23),
        (14, 16, 25, 26),
        (11, 12, 13, 19),
    )
    ans = recur(state_ques)
    print(ans)


if __name__ == "__main__":
    main()
