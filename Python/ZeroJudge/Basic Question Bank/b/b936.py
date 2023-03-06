"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b936
Title: Kevin 愛橘子
"""

"""
分析之後可以發現N為奇數時有多次重複的遞迴，故N為奇數時可以一次展開兩層

N is even: f(n) = f(n / 2) + f(n / 2) = 2 * f(n / 2)
n is odd:  f(n) = f((n - 1) / 2) + f((n + 1) / 2)
            -> ((n - 1) / 2) is even: = (f((n - 1) / 4) + f((n - 1) / 4)) + (f(((n + 1) / 2 - 1) / 2) + f(((n + 1) / 2 + 1) / 2))
                                      = (f((n - 1) / 4) + f((n - 1) / 4)) + (f((n - 1) / 4) + f((n + 3) / 4))
                                      = 3 * f((n - 1) / 4) + f((n + 3) / 4)
            -> ((n - 1) / 2) is odd:  = (f(((n - 1) / 2 - 1) / 2) + f(((n - 1) / 2 + 1) / 2)) + (f((n + 1) / 4) + f((n + 1) / 4))
                                      = (f((n - 3) / 4) + f(n + 1) / 4) + (f((n + 1) / 4) + f(n + 1) / 4)
                                      = f((n - 3) / 4) + 3 * f((n + 1) / 4)

0 <= n < m: return 0
m <= n < 2m: return 1
2m <= n < 4m - 2: return 2
"""


def DFS(n, m):
    if 0 <= n < m:
        return 0
    if m <= n < 2 * m:
        return 1
    if 2 * m <= n < 4 * m - 2:
        return 2

    if n % 2 == 0:
        return 2 * DFS(n // 2, m)
    if n % 2 == 1:
        if (n - 1) // 2 % 2 == 0:
            return 3 * DFS((n - 1) // 4, m) + DFS((n + 3) // 4, m)
        if (n - 1) // 2 % 2 == 1:
            return DFS((n - 3) // 4, m) + 3 * DFS((n + 1) // 4, m)


while True:  # TODO NA (score:59%)
    try:
        N, M = map(int, input().split())
    except EOFError:
        break

    print(DFS(N, M))
