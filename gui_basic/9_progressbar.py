import tkinter.ttk as tk
from tkinter import *
import time

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = tk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = tk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 초 마다 움직임
# progressbar.pack()

# def btncmd():
#   progressbar.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = tk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd():
  for i in range(1, 101):
    time.sleep(0.01)
    p_var2.set(i) # progressbar 값 설정
    progressbar2.update()   # ui 업데이트
    print(p_var2.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()


root.mainloop()