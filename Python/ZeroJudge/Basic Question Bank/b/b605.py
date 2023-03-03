"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b605
Title: Package
"""

from math import ceil

while True:
    str = input()

    if str == "-1":
        break

    li = list(map(int, str.split()))

    length = 0  # 邊長

    space = 0  # 剩餘空間
    for i in range(
        6, 0 - 1, -1
    ):  # 從大的產品算到小的產品，原本1單位=n長度 -> 1單位=n/2長度，也就是說同樣長度下1單位 -> 2單位
        length *= 2
        space *= 4

        space -= li[i]
        if space < 0:
            """
            邊長要變為(length + n)
            -> (length + n)^2 - length^2 >= -space, 2 * length * n + n^2 + space >= 0

            n^2 + 2 * length * n + space >= 0
            n >= (-(2 * length) + ((2 * length)^2 - 4 * 1 * space)^0.5) / (2 * 1), n >= (-2 * length + ((2 * length)^2 - 4 * space)^0.5) / 2
            """

            n = ceil((-2 * length + ((2 * length) ** 2 - 4 * space) ** 0.5) / 2)

            length += n
            space += (length + n) ** 2 - length**2

    print(length)
