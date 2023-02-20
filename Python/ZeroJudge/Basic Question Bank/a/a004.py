"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a004
Title: 文文的求婚
"""

while True:
    try:
        y = int(input())
    except EOFError:
        break

    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("閏年")
    else:
        print("平年")
