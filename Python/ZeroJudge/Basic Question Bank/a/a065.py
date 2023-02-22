"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a065
Title: 提款卡密碼
"""

str = input()

for i in range(1, len(str)):
    print(abs(ord(str[i]) - ord(str[i - 1])), end="")
