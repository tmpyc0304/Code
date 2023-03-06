"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a020
Title: 身分證檢驗
"""

dic = {
    "A": 1,
    "B": 10,
    "C": 19,
    "D": 28,
    "E": 37,
    "F": 46,
    "G": 55,
    "H": 64,
    "I": 39,
    "J": 73,
    "K": 82,
    "L": 2,
    "M": 11,
    "N": 20,
    "O": 48,
    "P": 29,
    "Q": 38,
    "R": 47,
    "S": 56,
    "T": 65,
    "U": 74,
    "V": 83,
    "W": 21,
    "X": 3,
    "Y": 12,
    "Z": 30,
}

str = input()

s = dic[str[0]]
for i in range(1, len(str) - 1):
    s += (8 - i + 1) * int(str[i])
s += int(str[-1])

if s % 10 == 0:
    print("real")
else:
    print("fake")
