"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b557
Title: 直角三角形
"""

from collections import Counter
from itertools import combinations

T = int(input())
for i in range(T):
    N = int(input())
    dic = Counter(sorted(list(map(int, input().split()))))

    s = 0
    for j in combinations(dic, 2):  # 取3個會TLE
        if (j[0] ** 2 + j[1] ** 2) ** 0.5 in dic:
            s += dic[j[0]] * dic[j[1]] * dic[int((j[0] ** 2 + j[1] ** 2) ** 0.5)]

    print(s)
