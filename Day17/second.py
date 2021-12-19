import sys


def main():
    x_start, x_end = 111, 161
    y_start, y_end = -154, -101

    # x_start, x_end = 20, 30
    # y_start, y_end = -10, -5

    count = 0

    for x_vel in range(0, 200):
        for y_vel in range(-160, 5000, 1):
            x = 0
            y = 0
            d_x = x_vel
            d_y = y_vel

            while x <= x_end and y >= y_start:
                x += d_x
                y += d_y

                if d_x > 0:
                    d_x -= 1
                d_y -= 1
                if x_vel == 6 and y_vel == 7:
                    print("->", x, y)

                if x_start <= x <= x_end and y_start <= y <= y_end:
                    count += 1
                    print(x_vel, y_vel)
                    break

    print(count)


if __name__ == "__main__":
    main()
