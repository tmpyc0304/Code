"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a147
Title: Print it all
"""

while True:
    n = int(input())

    if n == 0:
        break

    print(*[i for i in range(n) if i % 7 != 0])
