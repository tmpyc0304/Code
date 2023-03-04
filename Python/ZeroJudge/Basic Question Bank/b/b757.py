"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b757
Title: 頸美椰子樹
"""

while True:
    try:
        r = float(input())
    except EOFError:
        break

    print(f"{(r * 9 / 5 + 32):g}")
