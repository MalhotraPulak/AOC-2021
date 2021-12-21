import functools


@functools.lru_cache(maxsize=None)
def winning_universes(score1, score2, turn, loc1, loc2):
    if score1 >= 21:
        return 1

    if score2 >= 21:
        return 0

    # print(score1, score2, turn, loc1, loc2)

    winning_univ = 0

    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                if turn == 0:
                    summ = loc1
                else:
                    summ = loc2

                summ += i + j + k
                # print(
                #     f"Player {turn} rolled {i + j + k}, {loc1=} {loc2=} {score1=} {score2=}"
                # )
                new_loc = (summ - 1) % 10 + 1
                if turn == 0:
                    winning_univ += winning_universes(
                        score1 + new_loc,
                        score2,
                        1 - turn,
                        new_loc,
                        loc2,
                    )
                else:
                    winning_univ += winning_universes(
                        score1,
                        score2 + new_loc,
                        1 - turn,
                        loc1,
                        new_loc,
                    )

    return winning_univ


def main():
    s1, s2 = 2, 5

    ans = winning_universes(0, 0, 0, s1, s2)
    ans2 = winning_universes(0, 0, 0, s1, s2)

    print(max(ans, ans2))


if __name__ == "__main__":
    main()
