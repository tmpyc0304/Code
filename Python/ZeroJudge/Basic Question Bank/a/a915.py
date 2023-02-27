"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a915
Title: 二维点排序
"""

n = int(input())

li = []

for i in range(n):
    li.append(list(map(int, input().split())))

for i in sorted(li):
    print(*i)
