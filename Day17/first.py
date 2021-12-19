import sys


def main():
    x_start, x_end = 111, 161
    y_start, y_end = -154, -101

    # x_start, x_end = 20, 30
    # y_start, y_end = -10, -5

    y_max = 0

    for x_vel in range(-1000, 200, 1):
        for y_vel in range(1000):
            x = 0
            y = 0
            d_x = x_vel
            d_y = y_vel

            landed = False
            local_y_max = 0
            while x <= x_end and y >= y_end:
                x += d_x
                y += d_y
                local_y_max = max(local_y_max, y)

                if d_x > 0:
                    d_x -= 1
                elif d_x < 0:
                    d_x += 1

                d_y -= 1

                if x_start <= x <= x_end and y_start <= y <= y_end:
                    landed = True

            if landed:
                y_max = max(y_max, local_y_max)

    print(y_max)


if __name__ == "__main__":
    main()
