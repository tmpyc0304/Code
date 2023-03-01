"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b374
Title: [福州19中]众数
"""

from collections import Counter

N = int(input())
dic = Counter(list(map(int, input().split())))

max_num = max([dic[key] for key in dic])

for i in sorted([key for key in dic if dic[key] == max_num]):
    print(i, max_num)
