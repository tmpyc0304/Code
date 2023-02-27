"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a740
Title: 质因数之和
"""

while True:
    try:
        x = int(input())
    except EOFError:
        break

    s = 0
    while x % 2 == 0:  # 2
        s += 2
        x //= 2

    while x % 3 == 0:  # 3
        s += 3
        x //= 3

    for i in range(6, int(x**0.5) + 1, 6):
        while x % (i - 1) == 0:
            s += i - 1
            x //= i - 1

        while x % (i + 1) == 0:
            s += i + 1
            x //= i + 1

    if x != 1:
        s += x

    print(s)
