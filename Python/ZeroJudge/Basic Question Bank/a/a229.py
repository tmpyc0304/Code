"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a229
Title: 括號匹配問題
"""


def DFS(str, L, R, n):
    if L < R or L > n or R > n:
        return

    if L == R == n:
        print(str)

        return

    DFS(str + "(", L + 1, R, n)
    DFS(str + ")", L, R + 1, n)


while True:  # TODO TLE (3s)
    try:
        N = int(input())
    except EOFError:
        break

    DFS("", 0, 0, N)
