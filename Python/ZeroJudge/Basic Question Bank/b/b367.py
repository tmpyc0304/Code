"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b367
Title: 翻轉世界
"""

T = int(input())
for i in range(T):
    N, M = map(int, input().split())

    li1, li2 = [], []
    for i in range(N):
        tmp = list(map(int, input().split()))

        li1.append(tmp)
        li2.insert(0, tmp[::-1])

    if li1 == li2:
        print("go forward")
    else:
        print("keep defending")
