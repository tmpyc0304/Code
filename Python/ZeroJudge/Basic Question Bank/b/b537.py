"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b537
Title: 分數運算-1
"""

from fractions import Fraction

"""
f(1) = 1
k is even: f(k) = 1 + f(k / 2) > 1
k is odd:  f(k) = 1 / f(k - 1)
           又(k - 1) is even -> f(k - 1) > 1
           -> f(k) < 1
"""


def getk(n):
    if n == 1:
        return 1
    if n > 1:
        return getk(n - 1) * 2
    if n < 1:
        return getk(1 / n) + 1


while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    print(getk(Fraction(a, b)))
