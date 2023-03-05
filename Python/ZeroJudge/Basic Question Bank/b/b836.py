"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b836
Title: kevin戀愛攻略系列題-2 說好的霸王花呢??
"""

while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break

    if m == 0:  # 最後一筆測資的m = 0，造成跑太多圈而TLE
        print("Go Kevin!!")
    else:
        i = 0
        while n > 0:
            n -= 1 + i * m
            i += 1

        if n == 0:
            print("Go Kevin!!")
        else:
            print("No Stop!!")
