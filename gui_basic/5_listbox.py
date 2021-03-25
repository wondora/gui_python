from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) # single 하나만 선택
listbox.insert(0, "사과0")
listbox.insert(1, "사과1")
listbox.insert(2, "사과2")
listbox.insert(END, "포도")
listbox.insert(END, "수박")
listbox.pack()

def btncmd():
  # listbox.delete(END)
  # listbox.delete(0) # 맨 처음부터 삭제

  # print(" 리스트 갯수 : ", listbox.size())

  # 항목 확인
  # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

  # 선택된 항목 확인 (인덱스 값 반환 : 0, 1, 2....)
  print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="CLICK", command=btncmd)
btn.pack()

root.mainloop()