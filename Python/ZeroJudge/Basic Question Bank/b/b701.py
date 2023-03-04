"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b701
Title: 我的領土有多大
"""

from queue import Queue

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右、下、左、上


def in_bound(x, y, X, Y, ma):
    if 0 <= x < Y and 0 <= y < X and ma[x][y] == '1':
        return True
    return False


X, Y = map(int, input().split())  # 注意此題為直角坐標
ma = [list(input().split()) for i in range(Y)]

for i in range(Y):
    for j in range(X):
        if in_bound(i, j, X, Y, ma) is True:
            W, N, E, S, c = j, i, j, i, 0

            coo = Queue()
            ma[i][j] = '2'
            coo.put([i, j])
            while coo.empty() is False:  # BFS
                x, y = coo.get()

                W = min(W, y)
                N = min(N, x)
                E = max(E, y)
                S = max(S, x)
                c += 1

                for k in range(4):
                    if in_bound(x + dir[k][0], y + dir[k][1], X, Y, ma) is True:
                        ma[x + dir[k][0]][y + dir[k][1]] = '2'
                        coo.put([x + dir[k][0], y + dir[k][1]])

            print(W, N, E, S, c)
