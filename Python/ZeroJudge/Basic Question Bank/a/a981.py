"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a981
Title: 求和問題
"""

from itertools import combinations

"""
https://www.youtube.com/watch?v=VizVXAyhAAM&ab_channel=davidchien
此題用DFS會TLE
"""

n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))

li1 = li[:(len(li) // 2)]
li2 = li[(len(li) // 2):]

com = {}
for i in range(1, len(li2) + 1):  # 因為前半部是用二進制模擬數字的選擇與否，所以必須先窮舉後半部，才能符合題意的由小到大輸出
    for tmp in combinations(li2, i):
        if sum(tmp) <= m:
            try:
                com[sum(tmp)].append(tmp)
            except KeyError:
                com[sum(tmp)] = [tmp]
for i in com.keys():  # 排序每個總和的可能組合(由小到大)
    com[i].sort()

find = False
for i in range(2 ** len(li1) - 1, 0 - 1, -1):  # 用二進制模擬該數字的選擇與否，從大到小的二進制才能符合題意的由小到大輸出
    choose = bin(i)[2:].zfill(len(li1))
    tmp = [a for a, b in zip(li1, choose) if b == "1"]

    if sum(tmp) == m:
        print(*tmp)

        find = True
    elif sum(tmp) < m:
        if (m - sum(tmp)) in com.keys():
            for j in com[m - sum(tmp)]:
                print(*tmp, *j)

            find = True

if find is False:
    print(-1)
