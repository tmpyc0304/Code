"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b373
Title: [福州19中]车厢重组
"""

N = int(input())

li = []
while True:  # 數列測資可能不在同一行
    try:
        li += list(map(int, input().split()))
    except EOFError:
        break

s = 0
for i in range(N):
    s += sum(li[i] > j for j in li[(i + 1):])

print(s)
