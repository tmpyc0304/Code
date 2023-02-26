"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a528
Title: 大數排序
"""

while True:
    try:
        N = int(input())
    except EOFError:
        break

    for i in sorted([int(input()) for i in range(N)]):
        print(i)
