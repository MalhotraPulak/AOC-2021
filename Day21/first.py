def main():
    s1, s2 = 2, 5

    score1 = 0
    score2 = 0
    die = 1
    roll = 0
    while score1 < 1000 and score2 < 1000:
        for _ in range(3):
            roll += 1
            s1 += die
            die = die % 100 + 1
        score1 += (s1 - 1) % 10 + 1

        if score1 >= 1000:
            break

        for _ in range(3):
            roll += 1
            print(die)
            s2 += die
            die = die % 100 + 1
        score2 += (s2 - 1) % 10 + 1
        print(score1, score2)

    print(roll * min(score1, score2))


if __name__ == "__main__":
    main()
