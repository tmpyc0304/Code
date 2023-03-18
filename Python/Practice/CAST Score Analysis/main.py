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

tk.Label(frame1, text="輸入學測成績").grid(row=0, column=0, sticky=tk.W)
for i in range(1, 6 + 1):
    exec(f"score{i} = tk.IntVar()")
    exec(f"frame1_{i} = tk.Frame(frame1)")
    exec(f"tk.Label(frame1_{i}, text='{analysis.subject[i]}').pack(side='left')")
    exec(f"tk.Entry(frame1_{i}, textvariable=score{i}, width=2).pack(side='left')")
    exec(f"frame1_{i}.grid(row=0, column={i}, sticky=tk.W)")

tk.Label(frame1, text="輸入分科成績").grid(row=1, column=0, sticky=tk.W)
for i in range(7, 13 + 1):
    exec(f"score{i} = tk.IntVar()")
    exec(f"frame1_{i} = tk.Frame(frame1)")
    exec(f"tk.Label(frame1_{i}, text='{analysis.subject[i]}').pack(side='left')")
    exec(f"tk.Entry(frame1_{i}, textvariable=score{i}, width=2).pack(side='left')")
    exec(f"frame1_{i}.grid(row=1, column={i - 6}, sticky=tk.W)")

frame1.grid(row=1, column=0, sticky=tk.W)

# 確定成績
score = []


def input_score():
    for i in range(1, 13 + 1):
        score.append(eval(f"score{i}.get()"))


frame2 = tk.Frame(main_frame)

button1 = tk.Button(
    frame2,
    text="確定",
    command=lambda: [
        button1.destroy(),
        input_score(),
        label1.pack(side="left"),
        analysis.create_dic(),
        frame3.grid(row=3, column=0, sticky=tk.W),
        frame4.grid(row=4, column=0, sticky=tk.W),
    ],
)
label1 = tk.Label(frame2, text="成績輸入完成")

button1.pack(side="left")

frame2.grid(row=2, column=0, sticky=tk.W)

# 依大學篩選
frame3 = tk.LabelFrame(main_frame, text="依大學篩選")

frame3_1 = tk.Frame(frame3)
tk.Label(frame3_1, text="公立大學").grid(row=0, column=0, sticky=tk.W)
j, k = 1, 0
for i in range(1, 31 + 1):
    exec(f"college{i} = tk.StringVar()")
    exec(
        f"tk.Checkbutton(frame3_1, text='{analysis.public_college[i]}', variable=college{i}, onvalue='{analysis.public_college[i]} ', offvalue='').grid(row={j}, column={k}, sticky=tk.W)"
    )

    k += 1

    j += k // 5
    k %= 5
frame3_1.grid(row=0, column=0, sticky=tk.W)

frame3_2 = tk.Frame(frame3)
tk.Label(frame3_2, text="私立大學").grid(row=0, column=0, sticky=tk.W)
j, k = 1, 0
for i in range(1, 31 + 1):
    exec(f"college{i + 31} = tk.StringVar()")
    exec(
        f"tk.Checkbutton(frame3_2, text='{analysis.private_college[i]}', variable=college{i + 31}, onvalue='{analysis.private_college[i]} ', offvalue='').grid(row={j}, column={k}, sticky=tk.W)"
    )

    k += 1

    j += k // 5
    k %= 5
frame3_2.grid(row=1, column=0, sticky=tk.W)


# 開始分析
def create_list():
    select = ""
    for i in range(1, 62 + 1):
        select += eval(f"college{i}.get()")

    global admit
    admit = analysis.calculate_weight(score, select)


frame4 = tk.Frame(main_frame)

button2 = tk.Button(
    frame4,
    text="開始分析",
    command=lambda: [
        button2.destroy(),
        create_list(),
        label2.pack(side="left"),
        show(),
        frame5.grid(row=5, column=0, sticky=tk.W),
    ],
)
label2 = tk.Label(frame4, text="分析完成")

button2.pack(side="left")


# 顯示錄取校系
def show():
    for i in range(len(admit)):
        tk.Label(frame5, text=admit[i]["系組代碼"]).grid(row=i, column=0, sticky=tk.W)
        tk.Label(frame5, text=admit[i]["校名"]).grid(row=i, column=1, sticky=tk.W)
        tk.Label(frame5, text=admit[i]["系組名"]).grid(row=i, column=2, sticky=tk.W)


frame5 = tk.Frame(main_frame)

# 滑動設定
main_frame.bind(
    "<Configure>",
    lambda event: canvas.config(
        scrollregion=canvas.bbox("all")
    ),  # 動態規劃滑動範圍，因為要包含上面的所有元素，所以要放在最下面，不加event(可改)會沒效果不知道為什麼
)
canvas.pack()

root.mainloop()
