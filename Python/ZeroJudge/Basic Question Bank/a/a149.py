"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a149
Title: 乘乘樂
"""

T = int(input())
for i in range(T):
    str = input()

    s = 1
    for j in str:
        s *= int(j)

    print(s)
