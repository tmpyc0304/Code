"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b924
Title: kevin 愛畫畫
"""

while True:  # TODO NA (score:91%)
    try:
        str = input()
    except EOFError:
        break

    if str.split() == "":
        continue

    n, m = map(int, str.split())

    c1 = [0 for i in range(n + 1)]  # 進入的邊+離開的邊

    for i in range(m):
        a, b = map(int, input().split())

        c1[a] += 1
        c1[b] += 1

    c2 = sum([1 for i in c1 if i % 2 == 1])
    if c2 == 0 or c2 == 2:  # 只會是全封閉或一起點一終點
        print("YES")
    else:
        print("NO")
