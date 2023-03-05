"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b893
Title: 勘根定理
"""

"""
-2147483647<= x^6 <= 2147483647
-> (-36 ~ -35.9) <= x <= (35.9 ~ 36) -> 從-36跑到36
"""

a, b, c, d, e, f = map(int, input().split())

if a == b == c == d == e == f:
    print('Too many... = ="')
else:
    find = False

    pre = (
        a * (-36) ** 5 + b * (-36) ** 4 + c * (-36) ** 3 + d * (36) ** 2 + e * (-36) + f
    )
    if pre == 0:
        print(-36, -36)

        find = True
    for i in range(-35, 36 + 1):
        n = a * i**5 + b * i**4 + c * i**3 + d * i**2 + e * i + f

        if n == 0:
            print(i, i)

            find = True
        elif pre * n < 0:
            print(i - 1, i)

            find = True

        pre = n

    if find is False:
        print("N0THING! >\\\\\\<")  # 要三個\才對，題目給錯
