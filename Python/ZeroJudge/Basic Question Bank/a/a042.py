"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a042
Title: 平面圓形切割
"""

while True:
    try:
        n = int(input())
    except EOFError:
        break

    print(n**2 - n + 2)
