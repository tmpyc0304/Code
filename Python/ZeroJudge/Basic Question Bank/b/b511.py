"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b511
Title: 換銅板
"""


def DFS(ans, s, n, li):
    if len(ans) == n:
        if s == 0:
            print("(" + ",".join(list(map(str, ans))) + ")")

        return

    for i in range(s // li[len(ans)] + 1):
        DFS(ans + [i], s - i * li[len(ans)], n, li)


N = int(input())
li = list(map(int, input().split()))
max_num = int(input())

DFS([], max_num, N, li)
