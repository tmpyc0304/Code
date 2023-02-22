"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a104
Title: 排序
"""

while True:
    try:
        n = int(input())
    except EOFError:
        break

    print(*sorted(list(map(int, input().split()))))
