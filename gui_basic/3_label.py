from tkinter import *

root = Tk()
root.title("Nado GUI")

label1 = Label(root, text="안녕하세요")
label1.pack()

# photo = PhotoImage(file="......")
# label2 = Label(root, image=photo)
# label2.pack()

def change():
  label1.config(text="see you next!!")

  # global photo2 # 가베지 컬렉션은 지역변수는 사용 후 지운다. 그래서 전역 변수 선언
  # photo2 = PhotoImage(file=".....")
  # label2.config(image=photo)


btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()