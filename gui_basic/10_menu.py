from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

menu = Menu(root)


def create_new_file():
  print("새 파일을 만듭니다.")

# FIle menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window", command=create_new_file)
menu_file.add_separator()
menu_file.add_command(label="Open FIle...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) 
menu.add_cascade(label="FIle", menu=menu_file)

# Edit menu
menu.add_cascade(label="Edit")

# Language 메뉴 추가
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()