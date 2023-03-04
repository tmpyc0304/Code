"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b680
Title: 百米賽道編排
"""

N = int(input())

dic = {}
for i in range(N):
    str = input()
    dic[float(str.split()[1])] = int(str.split()[0])

li = [[] for i in range(N // 8 + 1)]

i = 0
time = sorted(dic)
for j in range(4):
    for k in range(1, N // 8 + 1):
        li[k].append(time[i])
        i += 1
    for k in range(N // 8, 1 - 1, -1):
        li[k].append(time[i])
        i += 1

"""
從1到8號跑者的跑道 -> 4 5 3 6 2 7 1 8
從1到8號跑道的跑者 -> 7 5 3 1 2 4 6 8
"""

for i in range(1, N // 8 + 1):
    print(
        i,
        dic[li[i][6]],
        dic[li[i][4]],
        dic[li[i][2]],
        dic[li[i][0]],
        dic[li[i][1]],
        dic[li[i][3]],
        dic[li[i][5]],
        dic[li[i][7]],
    )
