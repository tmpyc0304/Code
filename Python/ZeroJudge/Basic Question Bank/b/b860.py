"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b860
Title: 獨角蟲進化計算器
"""

c, w = map(int, input().split())

c_ans = 0
while c + w >= 13 and w >= 1:  # 進化一次至少需要12顆糖(蟲跟糖可互換) + 1隻蟲
    c -= 12
    if c < 0:
        w += c  # 用蟲換糖果
        c = 0
    w += 1  # 進化後的蟲
    c_ans += 1

print(c_ans)
