"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a215
Title: 明明愛數數
"""

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    i = 1  # n為第1項

    base = n
    while n <= m:
        n += base + i
        i += 1

    print(i)
