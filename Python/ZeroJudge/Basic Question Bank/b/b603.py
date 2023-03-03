"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b603
Title: 拋物線方程式
"""

from math import gcd

"""
y = a(x - h)^2 + k = ax^2 - 2ahx + (ah^2 + k)
a = (y - k) / (x - h)^2
去分母 -> (x - h)^2 * y = (y - k)x^2 + -2(y - k)hx + ((y - k)h^2 + (x - h)^2 * k)
"""

while True:
    try:
        x1, y1, x2, y2 = map(int, input().split())
    except EOFError:
        break

    a = (x2 - x1) ** 2
    b = y2 - y1
    c = -2 * (y2 - y1) * x1
    d = (y2 - y1) * x1**2 + (x2 - x1) ** 2 * y1

    a, b, c, d = map(
        lambda n: n // gcd(a, gcd(b, gcd(c, d))), [a, b, c, d]
    )  # ZeroJudge的Python版本太舊，gcd()只能接受兩個變數

    print(f"{a}y = {b}x^2 + {c}x + {d}")
