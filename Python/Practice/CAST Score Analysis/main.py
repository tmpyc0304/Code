import tkinter as tk

# Create window object
root = tk.Tk()

# Set window's title
root.title("CAST Score Analysis")

# Set window's size
window_width = root.winfo_screenwidth()  # 取得螢幕寬
window_height = root.winfo_screenheight()  # 取得螢幕高

width = window_width // 2
height = window_height // 2
top = window_width // 4
left = window_height // 4
root.geometry(f"{width}x{height}+{top}+{left}")

# Set label
tk.Label(root, text="分科測驗成績分析").grid(row=0, column=0, sticky=tk.W)

# Enter GSAT score
frame1 = tk.Frame(root)

tk.Label(frame1, text="輸入學測成績").pack(side="left")

chinese = tk.IntVar()
frame1_1 = tk.Frame(frame1)
tk.Label(frame1_1, text="國文").pack(side="left")
tk.Entry(frame1_1, textvariable=chinese, width=2).pack(side="left")
frame1_1.pack(side="left")

english = tk.IntVar()
frame1_2 = tk.Frame(frame1)
tk.Label(frame1_2, text="英文").pack(side="left")
tk.Entry(frame1_2, textvariable=english, width=2).pack(side="left")
frame1_2.pack(side="left")

mathA = tk.IntVar()
frame1_3 = tk.Frame(frame1)
tk.Label(frame1_3, text="數A").pack(side="left")
tk.Entry(frame1_3, textvariable=mathA, width=2).pack(side="left")
frame1_3.pack(side="left")

mathB = tk.IntVar()
frame1_4 = tk.Frame(frame1)
tk.Label(frame1_4, text="數B").pack(side="left")
tk.Entry(frame1_4, textvariable=mathB, width=2).pack(side="left")
frame1_4.pack(side="left")

frame1.grid(row=1, column=0, sticky=tk.W)

# Enter CAST score
frame2 = tk.Frame(root)

tk.Label(frame2, text="輸入分科成績").pack(side="left")

math1 = tk.IntVar()
frame2_1 = tk.Frame(frame2)
tk.Label(frame2_1, text="數甲").pack(side="left")
tk.Entry(frame2_1, textvariable=math1, width=2).pack(side="left")
frame2_1.pack(side="left")

history = tk.IntVar()
frame2_2 = tk.Frame(frame2)
tk.Label(frame2_2, text="歷史").pack(side="left")
tk.Entry(frame2_2, textvariable=history, width=2).pack(side="left")
frame2_2.pack(side="left")

geography = tk.IntVar()
frame2_3 = tk.Frame(frame2)
tk.Label(frame2_3, text="地理").pack(side="left")
tk.Entry(frame2_3, textvariable=geography, width=2).pack(side="left")
frame2_3.pack(side="left")

civics = tk.IntVar()
frame2_4 = tk.Frame(frame2)
tk.Label(frame2_4, text="公民").pack(side="left")
tk.Entry(frame2_4, textvariable=civics, width=2).pack(side="left")
frame2_4.pack(side="left")

physics = tk.IntVar()
frame2_5 = tk.Frame(frame2)
tk.Label(frame2_5, text="物理").grid(row=0, column=0)
tk.Entry(frame2_5, textvariable=physics, width=2).grid(row=0, column=1)
frame2_5.pack(side="left")

chemical = tk.IntVar()
frame2_6 = tk.Frame(frame2)
tk.Label(frame2_6, text="化學").pack(side="left")
tk.Entry(frame2_6, textvariable=chemical, width=2).pack(side="left")
frame2_6.pack(side="left")

biology = tk.IntVar()
frame2_7 = tk.Frame(frame2)
tk.Label(frame2_7, text="生物").pack(side="left")
tk.Entry(frame2_7, textvariable=biology, width=2).pack(side="left")
frame2_7.pack(side="left")

frame2.grid(row=2, column=0, sticky=tk.W)

root.mainloop()
