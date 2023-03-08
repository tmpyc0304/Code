"""
Problems: https://zerojudge.tw/ShowProblem?problemid=b982
Title: YoJudge 預練(空間之章)
"""

dic = {
    "g": "* 10 ** 9 * 8 +",
    "m": "* 10 ** 6 * 8 +",
    "k": "* 10 ** 3 * 8 +",
    "byte": "* 8 +",
    "bit": "* 1 +",
}

while True:
    try:
        str = input()
    except EOFError:
        break

    if "byte" in str:  # 修改帶有小數點的byte
        i = str.index("byte")
        if str[i - 2] == ".":
            str = str[: (i - 2)] + str[i:] + f"{str[i - 1]}bit"  # 移除小數點部分並在字串尾改成bit的形式

    print(
        int(
            eval(  # replace要注意先後順序
                str.replace("gb", dic["g"])
                .replace("g", dic["g"])
                .replace("mb", dic["m"])
                .replace("m", dic["m"])
                .replace("kb", dic["k"])
                .replace("k", dic["k"])
                .replace("byte", dic["byte"])
                .replace("bit", dic["bit"])
                .replace("b", dic["byte"])[:-1]  # 忽略最後一個'+'
            )
        )
    )
