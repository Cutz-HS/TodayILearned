# Q3+

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

# 함수선언
def openFile():
    global photo
    fileName = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    label1.configure(text=fileName)
    photo = PhotoImage(file = fileName)
    pLabel.configure(image=photo)
    pLabel.image = photo

def exitFile():
    window.quit()
    window.destroy()
    
def editFile(num):
    global photo
    if num == 1:
        value = askinteger('확대배수', '확대할 배수', minvalue=1, maxvalue=255)
        photo = photo.zoom(value, value)
        pLabel.configure(image=photo)
        pLabel.image = photo
    elif num == 2:
        value = askinteger('축소배수', '축소할 배수', minvalue=1, maxvalue=255)
        photo = photo.subsample(value, value)
        pLabel.configure(image=photo)
        pLabel.image = photo    
    
  
# 변수선언
window = None
photo = None

# main
window = Tk()
window.title("Memo")
window.geometry("700x700")
mainMenu = Menu(window)
window.config(menu=mainMenu)
label1 = Label(window)
label1.pack()

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="열기(O)...", command=lambda : openFile())
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)", command=lambda : exitFile())
fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 효과(E)", menu=fileMenu2)
fileMenu2.add_command(label="확대하기", command=lambda : editFile(1))
fileMenu2.add_command(label="축소하기", command=lambda : editFile(2))

# 빈 사진 준비
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand = 1, anchor = CENTER)

window.mainloop()