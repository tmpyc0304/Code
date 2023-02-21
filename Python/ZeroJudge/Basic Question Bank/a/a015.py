"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a015
Title: 矩陣的翻轉
"""

while True:  # 題目有多筆測資
    try:
        r, c = map(int, input().split())
    except EOFError:
        break

    A = [input().split() for i in range(r)]
    for i in range(c):
        print(*[A[j][i] for j in range(r)])
