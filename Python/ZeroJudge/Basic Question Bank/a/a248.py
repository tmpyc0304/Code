"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a248
Title: 新手訓練 ~ 陣列應用
"""

while True:
    try:
        a, b, N = map(int, input().split())
    except EOFError:
        break

    str = str(a * (10**N) // b)  # 避免四捨五入
    str = (N - len(str)) * "0" + str  # 位數不夠，前面補0

    a = str[:(-N)]  # 拆分，小數點前
    b = str[(-N):]  # 拆分，小數點後

    if a == "":  # 小數點後的位數為N位(小數點前沒有數字可以拆)
        a = "0"

    print(f"{a}.{b}")
