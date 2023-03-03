"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b604
Title: Center of Symmetry
"""

while True:
    n = int(input())

    if n == 0:
        break

    coo = sorted([list(map(int, input().split())) for i in range(n)])

    center = True

    cen_x = coo[0][0] + coo[-1][0]  # cen_x: center_x
    cen_y = coo[0][1] + coo[-1][1]  # cen_y: center_y
    for i in range(1, len(coo) // 2 + 1):
        if (
            coo[i][0] + coo[len(coo) - i - 1][0] != cen_x
            or coo[i][1] + coo[len(coo) - i - 1][1] != cen_y
        ):
            center = False

            break

    if center is True:
        print("yes")
    else:
        print("no")
