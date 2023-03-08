"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b971
Title: 等差數列
"""

a1, an, d = map(int, input().split())

if d > 0:
    an += 1
else:
    an -= 1

print(*[i for i in range(a1, an, d)])
