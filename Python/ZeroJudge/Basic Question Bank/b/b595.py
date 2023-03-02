"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b595
Title: Special Touring Car Racing
"""

while True:
    n = int(input())

    if n == 0:
        break

    a = [0] + list(map(int, input().split()))

    pre = [-1 for i in range(n + 1)]  # pre[a] = b -> a點的前一點是b

    DP = [0x9F9F9F9F for i in range(n + 1)]
    DP[0] = 0
    for i in range(1, n + 1):
        for j in range(i):  # 從j點到i點
            if DP[i] > DP[j] + (200 - (a[i] - a[j])) ** 2:
                DP[i] = DP[j] + (200 - (a[i] - a[j])) ** 2
                pre[i] = j

    route = [n]
    i = n
    while pre[i] != -1:
        route.append(pre[i])
        i = pre[i]

    print(*route[::-1])
