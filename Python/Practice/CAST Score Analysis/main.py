import tkinter as tk

# Create window object
root = tk.Tk()

# set window's title
root.title("CAST Score Analysis")

# set window's size
window_width = root.winfo_screenwidth()  # 取得螢幕寬
window_height = root.winfo_screenheight()  # 取得螢幕高

width = window_width // 2
height = window_height // 2
top = window_width // 4
left = window_height // 4
root.geometry(f"{width}x{height}+{top}+{left}")

# set label
tk.Label(root, text="CAST Score Analysis", font=("Arial", width // 40)).pack()

root.mainloop()
