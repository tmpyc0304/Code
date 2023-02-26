"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a694
Title: 吞食天地二
"""

from itertools import accumulate

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    pre = [[0 for i in range(n + 1)]]
    for i in range(n):
        pre.append([0] + list(accumulate(list(map(int, input().split())))))
    for i in range(2, n + 1):
        for j in range(1, n + 1):
            pre[i][j] += pre[i - 1][j]

    for i in range(m):
        x1, y1, x2, y2 = map(int, input().split())

        print(pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1])
