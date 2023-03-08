"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b944
Title: 好想上廁所(男廁篇)
"""

n = int(input())

li = [[0, 0] for i in range(n + 2)]  # [人, 時間]
while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    for i in range(1, n + 1):  # 會寫在最上面是因為題目會有時間為0的輸入，但有要求當次時間為0也要輸出
        if li[i][0] != 0:  # 有人
            li[i][1] -= 1
            if li[i][1] <= 0:  # 上完了
                li[i] = [0, 0]
    i = 1
    while i <= n and (
        li[i - 1][1] != 0 or li[i][1] != 0 or li[i + 1][1] != 0
    ):  # 尋找位置上跟兩旁都沒有人的位置
        i += 1
    if i == n + 1:  # 沒找到
        i = 1
        while i <= n and li[i][1] != 0:  # 尋找位置上沒有人的位置
            i += 1
        if i == n + 1:  # 沒找到
            print("  Not enough")
        else:  # 有找到
            li[i] = [a, b]
    else:
        li[i] = [a, b]

    print("Number:", *[li[i][0] for i in range(1, n + 1)])
    print("  Time:", *[li[i][1] for i in range(1, n + 1)])
