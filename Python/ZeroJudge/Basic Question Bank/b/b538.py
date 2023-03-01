"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b538
Title: 分數運算-2
"""

from fractions import Fraction  # 雖然沒有直接呼叫，但eval函式裡面有呼叫，所以還是要import

while True:
    try:
        str = input().split()
    except EOFError:
        break

    a, b, c, d = map(int, str[:4])

    print(
        eval(f"Fraction(a, b) {str[4]} Fraction(c, d)")
    )  # Fraction寫在{}裡面eval會視為'/'(除法)
