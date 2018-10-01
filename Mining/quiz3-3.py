# Q3

from tkinter import *

# 함수선언
def myFunc():
    if rVar.get() == 1:
        labelImage.configure(image=photo1)
    elif rVar.get() == 2:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)


# 변수선언
window = None
photo1, photo2, photo3 = [None]*3
rVar = 0
labelImage = None

# main
window = Tk()
window.title("애완동물 선택하기")
window.geometry("500x500")
labelTxt = Label(window, text="좋아하는 동물 투표", fg="red", font=("바탕체", 20))

rVar = IntVar()
rb1 = Radiobutton(window, text="강아지", variable=rVar, value=1) # 누르면 1번
rb2 = Radiobutton(window, text="토끼", variable=rVar, value=2)
rb3 = Radiobutton(window, text="고양이", variable=rVar, value=3)
btn = Button(window, text="사진 보기", command=myFunc)

photo1 = PhotoImage(file = "D:/data/gif/dog.gif")
photo2 = PhotoImage(file = "D:/data/gif/rabbit.gif")
photo3 = PhotoImage(file = "D:/data/gif/cat3.gif")

labelImage = Label(window, width=200, height=200, bg="gray", image=None)

labelTxt.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
btn.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)
window.mainloop()