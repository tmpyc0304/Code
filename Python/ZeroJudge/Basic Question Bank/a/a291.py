"""
Problems: https://zerojudge.tw/ShowProblem?problemid=a291
Title: nAnB problem
"""

from sys import stdin

output = ""
for input in stdin:  # TODO TLE (3s)
    if input.strip() == "":
        continue

    answer = list(map(int, input.split()))
    for i in range(int(stdin.readline())):
        guess = list(map(int, stdin.readline().split()))

        cA, cB = 0, 0
        count_answer, count_guess = [0 for j in range(10)], [0 for j in range(10)]
        for j in range(len(guess)):
            if answer[j] == guess[j]:  # nA
                cA += 1
            else:  # nB
                # 前面先找到未匹配的正確數字
                if count_answer[guess[j]] != 0:  # 匹配
                    cB += 1
                    count_answer[guess[j]] -= 1
                else:  # 匹配
                    count_guess[guess[j]] += 1
                # 前面先找到未匹配的猜測數字
                if count_guess[answer[j]] != 0:  # 匹配
                    cB += 1
                    count_guess[answer[j]] -= 1
                else:
                    count_answer[answer[j]] += 1

        output += f"{cA}A{cB}B\n"

print(output)
