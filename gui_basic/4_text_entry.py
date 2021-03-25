from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)  # 한줄 입력
e.pack()
e.insert(0, "한줄만 입력하세요") # 0 이나 END 가능 현재 값이 비어 있으므로

def btncmd():
  print(txt.get("1.0", END)) # 1 라인, 0 컬럼 : 즉 처음부터 끝까지(END)
  print(e.get())

  # 내용 삭제
  txt.delete("1.0", END)
  e.delete(0, END)

btn = Button(root, text="CLICK", command=btncmd)
btn.pack()

root.mainloop()