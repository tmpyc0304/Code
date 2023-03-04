"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b758
Title: 牛仔(ㄗˇ)很忙
"""

X, Y = map(int, input().split())

Y += 150
X = (X + Y // 60) % 24
Y %= 60

print(f"{X:02}:{Y:02}")
