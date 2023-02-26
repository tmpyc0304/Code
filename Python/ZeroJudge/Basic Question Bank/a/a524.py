"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a524
Title: 手機之謎
"""

from itertools import permutations

while True:
    try:
        n = int(input())
    except ValueError:  # 此題無EOF
        break

    for i in permutations([str(i) for i in range(n, 1 - 1, -1)]):
        print("".join(i))
