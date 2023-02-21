"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a010
Title: 因數分解
"""

n = int(input())

find = False

c = 0
while n % 2 == 0:  # 2
    c += 1
    n //= 2
if c > 0:
    print(2, end="")
    if c > 1:
        print(f"^{c}", end="")

    find = True

c = 0
while n % 3 == 0:  # 3
    c += 1
    n //= 3
if c > 0:
    if find is True:
        print(" * ", end="")
    print(3, end="")
    if c > 1:
        print(f"^{c}", end="")

    find = True

for i in range(6, int(n**0.5) + 1, 6):
    c = 0
    while n % (i - 1) == 0:  # i - 1
        c += 1
        n //= i - 1
    if c > 0:
        if find is True:
            print(" * ", end="")
        print(i - 1, end="")
        if c > 1:
            print(f"^{c}", end="")

        find = True

    c = 0
    while n % (i + 1) == 0:  # i + 1
        c += 1
        n //= i + 1
    if c > 0:
        if find is True:
            print(" * ", end="")
        print(i + 1, end="")
        if c > 1:
            print(f"^{c}", end="")

        find = True

if n != 1:
    if find is True:
        print(" * ", end="")
    print(n, end="")
