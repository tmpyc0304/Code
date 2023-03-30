import tkinter as tk
import analysis

# 創建視窗元件
root = tk.Tk()

# 設定視窗標題
root.title("CAST Score Analysis")

# 設定視窗大小
screen_width = root.winfo_screenwidth()  # 取得螢幕寬
screen_height = root.winfo_screenheight()  # 取得螢幕高

width = screen_width // 2
height = screen_height // 2
top = screen_width // 4
left = screen_height // 4

root.geometry(f"{width}x{height}+{top}+{left}")

# 創建有滑動條的畫布
canvas = tk.Canvas(root, width=width, height=height)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# 創建主群組
main_frame = tk.Frame(canvas)
canvas.create_window(0, 0, anchor=tk.NW, window=main_frame)

# 創建標籤
tk.Label(main_frame, text="分科測驗成績分析").grid(row=0, column=0, sticky=tk.W)

# 輸入成績
frame1 = tk.Frame(main_frame)

tk.Label(frame1, text="輸入學測級分").grid(row=0, column=0, sticky=tk.W)
tk.Label(frame1, text="輸入分科級分").grid(row=1, column=0, sticky=tk.W)

j = 0
for i in range(1, 13 + 1):
    exec(f"subject{i} = tk.IntVar()")
    exec(f"frame1_{i} = tk.Frame(frame1)")
    exec(f"tk.Label(frame1_{i}, text='{analysis.subject_list[i]}').pack(side='left')")
    exec(f"tk.Entry(frame1_{i}, textvariable=subject{i}, width=2).pack(side='left')")

    if i == 7:
        j = 1
    exec(f"frame1_{i}.grid(row={j}, column={i % 7 + j}, sticky=tk.W)")

frame1.grid(row=1, column=0, sticky=tk.W)


# 確定成績
def input_score():
    global score
    score = []

    for i in range(1, 13 + 1):
        score.append(eval(f"subject{i}.get()"))


tk.Button(
    main_frame,
    text="確定",
    command=lambda: [
        input_score(),
        analysis.create_dic(),
        frame2.grid(row=3, column=0, sticky=tk.W),
        frame3.grid(row=4, column=0, sticky=tk.W),
    ],
).grid(row=2, column=0, sticky=tk.W)


# 依大學篩選
click1 = False
click2 = False


def select_all1():
    global click1

    if click1 is False:
        for i in range(1, 31 + 1):
            exec(f"button{i}.select()")

            click1 = True
    else:
        for i in range(1, 31 + 1):
            exec(f"button{i}.deselect()")

            click1 = False


def select_all2():
    global click2

    if click2 is False:
        for i in range(1, 31 + 1):
            exec(f"button{i + 31}.select()")

            click2 = True
    else:
        for i in range(1, 31 + 1):
            exec(f"button{i + 31}.deselect()")

            click2 = False


frame2 = tk.LabelFrame(main_frame, text="依大學篩選")

tk.Checkbutton(frame2, text="公立全選", command=select_all1).grid(
    row=0, column=0, columnspan=5, sticky=tk.W
)
tk.Checkbutton(frame2, text="私立全選", command=select_all2).grid(
    row=8, column=0, columnspan=5, sticky=tk.W
)

j, k = 1, 0
for i in range(1, 62 + 1):
    if i == 32:
        j, k = 9, 0

    exec(f"college{i} = tk.StringVar()")
    exec(
        f"button{i} = tk.Checkbutton(frame2, text='{analysis.college_list[i]}', variable=college{i}, onvalue='{analysis.college_list[i]} ', offvalue='')"
    )
    exec(f"button{i}.grid(row={j}, column={k}, sticky=tk.W)")

    k += 1

    j += k // 5
    k %= 5


# 開始分析
def create_list():
    select = ""
    for i in range(1, 62 + 1):
        select += eval(f"college{i}.get()")

    global admit
    admit = sorted(
        analysis.calculate_weight(score, select),
        key=lambda d: d["滿分率"],
        reverse=True,
    )


frame3 = tk.Frame(main_frame)

tk.Button(
    frame3,
    text="開始分析",
    command=lambda: [
        create_list(),
        show(),
    ],
).pack(side="left")


# 顯示錄取校系
def show():
    global frame4

    frame4.destroy()

    frame4 = tk.Frame(main_frame)

    tk.Label(frame4, text="系組代碼").grid(row=0, column=0, sticky=tk.W)
    tk.Label(frame4, text="校名").grid(row=0, column=1, sticky=tk.W)
    tk.Label(frame4, text="系組名").grid(row=0, column=2, sticky=tk.W)
    tk.Label(frame4, text="錄取人數").grid(row=0, column=3, sticky=tk.W)
    tk.Label(frame4, text="錄取分數").grid(row=0, column=4, sticky=tk.W)
    tk.Label(frame4, text="錄取分數/滿分").grid(row=0, column=5, sticky=tk.W)
    tk.Label(frame4, text="加權分數").grid(row=0, column=6, sticky=tk.W)

    for i in range(len(admit)):
        tk.Label(frame4, text=admit[i]["系組代碼"]).grid(row=(i + 1), column=0, sticky=tk.W)
        tk.Label(frame4, text=admit[i]["校名"]).grid(row=(i + 1), column=1, sticky=tk.W)
        tk.Label(frame4, text=admit[i]["系組名"]).grid(row=(i + 1), column=2, sticky=tk.W)
        tk.Label(frame4, text=admit[i]["錄取人數"]).grid(row=(i + 1), column=3, sticky=tk.W)
        tk.Label(frame4, text=admit[i]["錄取分數"]).grid(row=(i + 1), column=4, sticky=tk.W)
        tk.Label(frame4, text=f"{admit[i]['滿分率']:.2f}%").grid(
            row=(i + 1), column=5, sticky=tk.W
        )
        tk.Label(frame4, text=admit[i]["加權分數"]).grid(row=(i + 1), column=6, sticky=tk.W)

    frame4.grid(row=5, column=0, sticky=tk.W)


frame4 = tk.Frame(main_frame)
frame4.grid(row=5, column=0, sticky=tk.W)

# 滑動設定
main_frame.bind(
    "<Configure>",
    lambda event: canvas.config(
        scrollregion=canvas.bbox("all")
    ),  # 動態規劃滑動範圍，因為要包含上面的所有元素，所以要放在最下面，不加event(可改)會沒效果不知道為什麼
)
canvas.pack()

root.mainloop()
