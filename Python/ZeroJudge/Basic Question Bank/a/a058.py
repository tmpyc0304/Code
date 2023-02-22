"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a058
Title: MOD3
"""

n = int(input())

c = [0 for i in range(3)]

for i in range(n):
    c[int(input()) % 3] += 1

print(*c)
