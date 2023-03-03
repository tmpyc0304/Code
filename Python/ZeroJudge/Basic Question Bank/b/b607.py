"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b607
Title: Number Partition
"""

prime = [2]
is_prime = [True for i in range(int(1000000**0.5) + 1)]  # 建完1000000會TLE

for i in range(3, int(1000000**0.5) + 1, 2):
    if is_prime[i] is True:
        for j in prime:
            if i % j == 0:
                is_prime[i] = False

                break
        if is_prime[i] is True:
            prime.append(i)

            for j in range(i * i, int(1000000**0.5) + 1, 2 * i):
                is_prime[j] = False


def is_Prime(n):
    if n in prime:
        return True

    for i in prime:  # n > int(100000000**0.5)
        if n % i == 0:
            return False
    return True


while True:
    n = int(input())

    if n == 0:
        break

    if is_Prime(n):  # n是質數
        print(1, n)
    elif n == 4:  # 特別判斷(2 + 2)
        print(2, 2, 2)
    elif n % 2 == 0:  # 偶數(奇 + 奇)
        x = n // 2 - (1 - n // 2 % 2)  # 小於等於(n / 2)的奇數
        for i in range(x, 0, -2):
            if is_Prime(i) is True and is_Prime(n - i) is True:
                print(2, i, n - i)

                break
    else:  # 奇數
        if is_Prime(n - 2) is True:  # 2 + (n - 2)
            print(2, 2, n - 2)
        else:  # 奇 + 奇 + 奇
            max_num = 0
            x = n // 3 - (1 - n // 3 % 2)  # 小於等於(n / 3)的奇數
            for i in range(x, x - 50, -2):  # 算到x - 50就好(再往下找的乘積也不會比較大，50是經測試後的最小值)
                if is_Prime(i) is True:
                    y = (n - i) // 2 - (1 - (n - i) // 2 % 2)  # 小於等於((n - i) / 2)的奇數
                    for j in range(y, i - 1, -2):
                        if is_Prime(j) is True and is_Prime(n - i - j) is True:
                            if i * j * (n - i - j) > max_num:
                                li = [i, j, n - i - j]
                                max_num = i * j * (n - i - j)
            print(3, *li)
