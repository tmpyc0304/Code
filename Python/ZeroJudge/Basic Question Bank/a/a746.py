"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a746
Title: 画蛇添足
"""

while True:
    try:
        str = input()
    except EOFError:
        break

    if str.strip() == "":  # 題目測資間應該有不正常的空行
        continue

    n, m = map(int, str.split())

    ma = []

    for i in range(n + 2):  # 邊界
        if i == 0 or i == n + 2 - 1:
            ma.append(["-" for i in range(n + 2)])
        else:
            ma.append(["|"] + [" " for i in range(n)] + ["|"])

    pre_x, pre_y = 0, 0
    for i in range(m):
        x, y = map(int, input().split())

        ma[x][y] = "*"
        if x == pre_x:
            for j in range(min(y, pre_y), max(y, pre_y)):
                ma[x][j] = "*"
        elif y == pre_y:
            for j in range(min(x, pre_x), max(x, pre_x)):
                ma[j][y] = "*"

        pre_x, pre_y = x, y

    for i in ma:
        print("".join(i))
