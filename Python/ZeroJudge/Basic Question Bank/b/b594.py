"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b594
Title: A Marvelous Pet
"""

"""
S = (a1 + an)n / 2 = (2a1 + (n - 1)d)n / 2
d = 1代入 -> S = (2a1 + (n - 1))n / 2 = (n^2 + (2a1 - 1)n) / 2
n^2 + (2a1 - 1)n - 2S = 0

a1 = 1時，n有最大值 -> n^2 + n - 2S = 0
n = (-1 +- (1^2 - 4 * 1 * (-2S))^0.5) / 2 = (-1 +- (1 + 8S)^0.5) / 2 (取正)

(2a1 - 1)n = 2S - n^2, a1 = (2S - n^2 + n) / 2n
"""

while True:
    n = int(input())

    if n == 0:
        break

    c = 0
    for i in range(2, int(-1 + (1 + 8 * n) ** 0.5) // 2 + 1):  # 跑連續的項數n，a1為整數即為合法解(a1開始連續n項，且不能只有1項)；如果跑a1從1 ~ (n / 2)，檢驗n是否為整數會TLE
        if ((2 * n - i ** 2 + i) / (2 * i)) % 1 == 0:  # if a1 % 1 == 0
            c += 1

    print(c)
