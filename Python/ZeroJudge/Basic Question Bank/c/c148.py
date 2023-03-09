"""
Problems: https://zerojudge.tw/ShowProblem?problemid=c148
Title: 機器人障礙賽
"""

from queue import Queue

dir = [[0, 1], [1, 0], [0, -1]]  # 右、下、左


def in_bound(x, y, n, m, ma):
    if 0 <= x < n and 0 <= y < m and ma[x][y] != -1:
        return True
    return False


while True:  # TODO NA (score:30%)
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    ma = [[0x9F9F9F9F for i in range(m)] for i in range(n)]

    b, e = map(int, input().split())

    for i in range(int(input())):
        x, y = map(int, input().split())

        ma[x][y] = -1

    coo = Queue()
    ma[0][b] = 0
    coo.put([0, b, 1, 0])  # [x, y, 前一個方向, 轉彎數]
    while coo.empty() is False:
        x, y, pre, c = coo.get()

        for i in range(3):
            if in_bound(x + dir[i][0], y + dir[i][1], n, m, ma):
                tmp = c
                if i != pre:
                    tmp += 1
                if ma[x + dir[i][0]][y + dir[i][1]] >= tmp:
                    ma[x + dir[i][0]][y + dir[i][1]] = tmp
                    coo.put([x + dir[i][0], y + dir[i][1], i, tmp])

    print(ma[n - 1][e])
