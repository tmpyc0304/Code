"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b884
Title: 電腦教室的傑克
"""

n = int(input())
for i in range(n):
    x, y = map(int, input().split())

    yee = 100 - (x + y)

    if 0 < yee <= 30:
        print("sad!")
    elif 30 < yee <= 60:
        print("hmm~~")
    elif 60 < yee < 100:
        print("Happyyummy")
    else:
        print("evil!!")
