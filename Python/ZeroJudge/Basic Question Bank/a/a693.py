"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a693
Title: 吞食天地
"""

from itertools import accumulate

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    pre = [0] + list(accumulate(list(map(int, input().split()))))

    for i in range(m):
        l, r = map(int, input().split())

        print(pre[r] - pre[l - 1])
