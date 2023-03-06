"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b911
Title: 我想跟Kevin借筷子系列4
"""

# 因為一刀可以砍無限根筷子，所以就砍原本最長的那一根就好，而最快的方法就是對半砍

while True:
    try:
        n = int(input())
    except EOFError:
        break

    c = 0
    while n > 0:
        n //= 2
        c += 1

    print(c)
