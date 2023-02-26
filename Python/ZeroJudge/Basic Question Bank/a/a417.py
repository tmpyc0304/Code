"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a417
Title: 螺旋矩陣
"""

dic = ["", "+", "-"]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右、下、左、上


def in_bound(x, y, N, ma):
    if 0 <= x < N and 0 <= y < N and ma[x][y] == 0:
        return True
    return False


T = int(input())
for i in range(T):
    N, M = map(int, input().split())

    ma = [[0 for i in range(N)] for j in range(N)]
    x, y = 0, 0
    c, i = 1, M - 1  # M = 1時i從0開始, M = 2時i從1開始
    while True:
        ma[x][y] = c

        if in_bound(x + dir[i][0], y + dir[i][1], N, ma) is False:
            i = eval(f"{i} {dic[M]} + 1") % 4
            if in_bound(x + dir[i][0], y + dir[i][1], N, ma) is False:
                break

        x += dir[i][0]
        y += dir[i][1]
        c += 1

    for j in ma:
        print("".join([f"{k:5d}" for k in j]))  # 測資的空格數是錯的
