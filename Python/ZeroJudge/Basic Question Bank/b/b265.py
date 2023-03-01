"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b265
Title: Q11286 - Conformity
"""

from itertools import groupby

while True:
    n = int(input())

    if n == 0:
        break

    li = sorted(["".join(sorted(input().split())) for i in range(n)])

    c = [len(list(val)) for key, val in groupby(li)]
    max_num = max(c)
    set_num = c.count(max_num)

    print(set_num * max_num)
