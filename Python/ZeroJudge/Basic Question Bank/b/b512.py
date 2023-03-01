"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b512
Title: 高維度稀疏向量
"""

dic1 = dict(map(lambda str: map(int, str.split(":")), input().split()))
dic2 = dict(map(lambda str: map(int, str.split(":")), input().split()))
# -> {dim1: value1, dim2: value2, ... }

s = 0
for key in dic1:
    if key in dic2:
        s += dic1[key] * dic2[key]

print(s)
