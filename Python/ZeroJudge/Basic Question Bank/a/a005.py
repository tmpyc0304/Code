"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a005
Title: Eva 的回家作業
"""

t = int(input())
for i in range(t):
    li = list(map(int, input().split()))

    if li[1] - li[0] == li[2] - li[1]:
        print(*li, li[3] + (li[1] - li[0]))
    else:
        print(*li, li[3] * (li[1] // li[0]))
