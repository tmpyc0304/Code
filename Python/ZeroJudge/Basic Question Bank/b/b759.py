"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b759
Title: 我明明就有說過= =
"""

X = input()

for i in range(len(X)):
    print(X[i:] + X[:i])
