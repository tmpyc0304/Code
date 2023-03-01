"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b294
Title: 經濟大恐荒
"""

n = int(input())
li = list(map(int, input().split()))

print(sum([(i + 1) * li[i] for i in range(n)]))
