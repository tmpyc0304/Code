"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b510
Title: M 皇后 N 城堡
"""

from copy import deepcopy

c = 0


def DFS(cQ, cC, m, n, ma):  # cQ: c_queen, cC: c_castle
    if cQ > m or cC > n:
        return

    if cQ == m and cC == n:
        global c
        c += 1

        return

    for i in range(m + n):  # 橫列上每個位置都試
        if ma[cQ + cC][i] == " ":
            tmp = deepcopy(ma)
            tmp[cQ + cC][i] = "q"  # 皇后

            for j in range(cQ + cC + 1, m + n):  # 往下每個橫列要做排除位置
                tmp[j][i] = "x"  # 下直線

                ver_dis = j - (cQ + cC)  # ver_dis: verticle_distance
                if 0 <= i - ver_dis:  # 左下斜
                    tmp[j][i - ver_dis] = "x"
                if i + ver_dis < m + n:  # 右下斜
                    tmp[j][i + ver_dis] = "x"

            DFS(cQ + 1, cC, m, n, tmp)

        if ma[cQ + cC][i] == " " or ma[cQ + cC][i] == "xq":
            tmp = deepcopy(ma)
            tmp[cQ + cC][i] = "c"  # 城堡

            for j in range(cQ + cC + 1, m + n):  # 往下每個橫列要做排除位置
                tmp[j][i] = "x"  # 下直線

                ver_dis = j - (cQ + cC)  # ver_dis: verticle_distance
                if 0 <= i - ver_dis:  # 左下斜
                    if tmp[j][i - ver_dis] != "x":
                        tmp[j][i - ver_dis] = "xq"  # 不能是皇后
                if i + ver_dis < m + n:  # 右下斜
                    if tmp[j][i + ver_dis] != "x":
                        tmp[j][i + ver_dis] = "xq"  # 不能是皇后

            DFS(cQ, cC + 1, m, n, tmp)


M, N = map(int, input().split())

DFS(0, 0, M, N, [[" " for i in range(M + N)] for j in range(M + N)])

print(c)
