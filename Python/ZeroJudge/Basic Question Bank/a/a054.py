"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a054
Title: 電話客服中心
"""

dic = ["BNZ", "AMW", "KLY", "JVX", "HU", "GT", "FS", "ER", "DOQ", "CIP"]

str = input()

s = sum([(8 - i) * int(str[i]) for i in range(len(str) - 1)])

print(dic[((10 - int(str[-1])) - s % 10) % 10])
