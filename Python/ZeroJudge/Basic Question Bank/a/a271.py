"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a271
Title: 彩色蘿蔔
"""

t = int(input())
for i in range(t):
    x, y, z, w, n, m = map(int, input().split())

    dic = [0, x, y, -z, -w]

    li = list(map(int, input().split()))

    c = 0
    for j in li:
        m -= c * n  # 中毒
        if m <= 0:  # 中毒出局
            break

        m += dic[j]  # 吃東西
        if m <= 0:  # 吃東西出局
            break

        if j == 4:  # 中毒疊加
            c += 1

    if m > 0:
        print(f"{m}g")
    else:
        print("bye~Rabbit")
