"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a647
Title: 投資專家
"""

n = int(input())
for i in range(n):
    m, p = map(int, input().split())

    r = (p - m) / m * 100

    if r > 0:  # 消除誤差(f-string的:.2f會無條件捨去，0.05有可能是0.04999...)，但不知道為什麼是0.00001
        r += 0.00001
    elif r < 0:
        r -= 0.00001

    if r >= 10 or r <= -7:
        print(f"{r:.2f}% dispose")
    else:
        print(f"{r:.2f}% keep")
