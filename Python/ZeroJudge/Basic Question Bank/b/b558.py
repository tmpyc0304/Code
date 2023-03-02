"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b558
Title: 求數列第 n 項
"""


def f(n):
    if n == 1:
        return 1

    return f(n - 1) + (n - 1)


while True:
    try:
        print(f(int(input())))
    except EOFError:
        break
