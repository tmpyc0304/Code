"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a059
Title: 完全平方和
"""

from math import ceil

T = int(input())
for i in range(1, T + 1):
    a = ceil(int(input()) ** 0.5)
    b = ceil(int(input()) ** 0.5)

    print(f"Case {i}: {sum([i ** 2 for i in range(a, b)])}")
