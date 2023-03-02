"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b592
Title: The Tower of Hanoi
"""

"""
https://naukri7707.github.io/%E7%B7%9A%E4%B8%8A%E8%A7%A3%E9%A1%8C/ZeroJudge/b592/
TODO 看可不可以圖像化
"""

# 此題盤子號碼最上面為1號
while True:
    n = int(input())

    if n == 0:
        break

    now = [0] + list(map(int, input().split()))  # now[m] = n -> 第m盤開始在第n根柱子
    end = [0] + list(map(int, input().split()))  # end[m] = n -> 第m盤結束在第n跟柱子

    while now[n] == end[n] and n > 0:
        n -= 1
    # 第n層以下(不包含)已經排好

    if n > 0:
        base = 1

        while now[base + 1] == now[1] and base + 1 != n:  # 連續子塔不用算到未排序的最後一個，因為最後一個是要移動的
            base += 1

        to = [0 for i in range(n + 1)]  # to[m] = n -> 第m盤要移動到第n根柱子
        to[n] = end[n]

        # 先整理
        for i in range(n, base, -1):  # to陣列排到base的所在層數，所以有base應該到的位置
            if now[i] == to[i]:  # 下面已經排好
                to[i - 1] = to[i]
            else:  # 下面還沒排好，上面的連續子塔要移到現在位置與目標位置之外
                to[i - 1] = 6 - now[i] - to[i]

        s = 0

        cur = now[base]  # cur: current現在連續子塔位置
        for i in range(base + 1, n + 1):  # 由上往下整理成一個完整的塔
            if now[i] == to[i]:  # 已經排好
                continue

            if now[i] + to[i] + cur == 6:  # 上面連續子塔已經讓位
                s += 1  # 直接移動第i盤
            else:
                s += 2**base  # (移開連續子塔 2 ** base - 1) + (移動第i盤 1) = 2 ** base
                base = i - 1
                cur = 6 - now[i] - to[i]

        # 再打亂
        cur = to[n - 1]
        for i in range(base, 0, -1):  # 從下到上
            if cur == end[i]:  # 已經排好
                continue

            s += 2 ** (i - 1)  # (移開連續子塔的步數 2 ** (i - 1) - 1) + (移開第i盤 1) = 2 ** (i - 1)
            cur = 6 - cur - end[i]

        print(s)
    else:
        print(0)
