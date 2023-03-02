"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b593
Title: Code
"""

com = [[0 for i in range(27)] for j in range(27)]  # com: combination


def combination(m, n):  # C m取n
    if com[m][n] != 0:
        return com[m][n]

    if m == n or n == 0:
        return 1
    if n == 1:
        return m

    com[m][n] = combination(m - 1, n - 1) + combination(m - 1, n)
    return com[m][n]


while True:
    str = input()

    if str == "0":
        break

    legal = True
    for i in range(1, len(str)):
        if str[i] <= str[i - 1]:
            legal = False

            break

    str = "`" + str  # 在前面加上a的前一位以利迴圈
    s = 0
    if legal is True:
        for i in range(1, len(str)):
            if i < len(str) - 1:  # 混合在同一個迴圈裡面簡化計算
                s += combination(26, i)

            for j in range(
                ord(str[i - 1]) - ord("a") + 1 + 1, ord(str[i]) - ord("a") + 1
            ):  # 小於該位英文的所有組合
                s += combination(
                    26 - j, len(str) - i - 1
                )  # (26 - j): 剩餘可選字母, (len(str) - i - 1): 剩餘位數(不算本位)
        s += 1  # 輸入的密碼

    print(s)
