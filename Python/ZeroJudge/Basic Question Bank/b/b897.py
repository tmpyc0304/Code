"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b897
Title: 10219 - Find the ways !
"""

from math import log, ceil

"""
log(a * b) = log(a) + log(b)
log(a / b) = log(a) - log(b)
"""

while True:
    try:
        n, k = map(int, input().split())
    except EOFError:
        break

    if n == k:
        print(1)
    else:
        s = 0
        for i in range(n, max(k, n - k), -1):
            s += log(i, 10)
        for i in range(min(k, n - k), 1 - 1, -1):
            s -= log(i, 10)

        print(ceil(s))
