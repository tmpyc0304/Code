"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b981
Title: YoJudge 預練(時間之章)
"""

dic = {
    "h": "* 60 * 60 * 1000 +",
    "m": "* 60 * 1000 +",
    "s": "* 1000 +",
    "ms": "* 1 +",
}

while True:
    try:
        print(
            int(
                eval(
                    input()  # replace要注意先後順序
                    .replace("hour", dic["h"])
                    .replace("h", dic["h"])
                    .replace("min", dic["m"])
                    .replace("ms", dic["ms"])
                    .replace("m", dic["m"])
                    .replace("s", dic["s"])[:-1]  # 忽略最後一個'+'
                )
            )
        )
    except EOFError:
        break
