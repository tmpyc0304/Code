"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b572
Title: 忘了東西的傑克
"""

N = int(input())
for i in range(N):
    H1, M1, H2, M2, time = map(int, input().split())

    if 60 * (H2 - H1) + (M2 - M1) >= time:
        print("Yes")
    else:
        print("No")
