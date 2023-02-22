"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a040
Title: 阿姆斯壯數
"""

n, m = map(int, input().split())

find = False
for i in range(n, m + 1):
    if sum([int(j) ** len(str(i)) for j in str(i)]) == i:
        print(i, end=" ")

        find = True

if find is False:
    print("none")
