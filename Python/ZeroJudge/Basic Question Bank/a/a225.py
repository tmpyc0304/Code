"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a225
Title: 明明愛排列
"""

while True:
    try:
        n = int(input())
    except EOFError:
        break

    li = ["0" + i for i in input().split()]  # 確保每個數字都是兩位數以上，s[:-1]才不會出錯

    li.sort(key=lambda n: int(n[:-1]), reverse=True)  # 先排序個位之外，由大到小
    li.sort(key=lambda n: int(n[-1]))  # 再排序個位，由小到大

    print(*[str(int(i)) for i in li])  # 轉成int再轉回str是為了消除左邊的0
