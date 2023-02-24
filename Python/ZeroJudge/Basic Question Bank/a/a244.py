"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a244
Title: 新手訓練 ~ for + if
"""

dic = ["", "+", "-", "*", "//"]

N = int(input())
for i in range(N):
    str = input().split()

    print(eval(str[1] + dic[int(str[0])] + str[2]))
