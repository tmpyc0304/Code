"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a148
Title: You Cannot Pass?!
"""

while True:
    try:
        li = list(map(int, input().split()))
    except EOFError:
        break

    if sum(li[1:]) / li[0] > 59:
        print("no")
    else:
        print("yes")
