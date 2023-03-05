"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b762
Title: 英國聯蒙
"""

dic = [
    "",
    "You have slain an enemie.",
    "You have slain an enemie.",
    "KILLING SPREE!",
    "RAMPAGE~",
    "UNSTOPPABLE!",
    "DOMINATING!",
    "GUALIKE!",
    "LEGENDARY!",
] + ["LEGENDARY!" for i in range(32)]

N = int(input())

c1, c2, c3, tmp = 0, 0, 0, 0
for i in range(N):
    str = input().strip()  # 輸入後會有空白

    if str == "Get_Kill":
        c1 += 1
        tmp += 1

        print(dic[tmp])
    elif str == "Die":
        c2 += 1

        if tmp < 3:
            print("You have been slained.")
        else:
            print("SHUTDOWN.")

        tmp = 0
    else:
        c3 += 1

print(f"{c1}/{c2}/{c3}")
