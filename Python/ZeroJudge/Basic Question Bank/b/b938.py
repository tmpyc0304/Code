"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b938
Title: kevin 愛殺殺
"""

n, m = map(int, input().split())  # TODO NA (score:50%)

li = [i + 1 for i in range(n + 1)]
alive = [True for i in range(n + 1)]
for i in map(int, input().split()):
    if alive[i] is True and li[i] <= n:
        if alive[li[i]] is True:
            print(li[i])

            alive[li[i]] = False
            while alive[li[i]] is False and li[i] < n:
                li[i] += 1
        else:
            print("0u0 ...... ?")
    else:
        print("0u0 ...... ?")
