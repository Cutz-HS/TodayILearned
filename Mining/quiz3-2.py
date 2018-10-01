# Q2

from tkinter import *

# 함수선언
def editFile(num):
    print(str(num) + ' 선택함.')


# 변수선언
window = None

# main
window = Tk()
window.title("Memo")
window.geometry("700x700")
mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일(F)", menu=fileMenu)
fileMenu.add_command(label="새로만들기(N)")
fileMenu.add_command(label="열기(O)...")
fileMenu.add_command(label="저장(S)")
fileMenu.add_command(label="다른이름으로 저장(A)...")
fileMenu.add_separator()
fileMenu.add_command(label="페이지 설정(U)...")
fileMenu.add_command(label="인쇄(P)")
fileMenu.add_separator()
fileMenu.add_command(label="끝내기(X)")
fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label="편집(E)", menu=fileMenu2)
fileMenu2.add_command(label="실행취소(U)")
fileMenu2.add_separator()
fileMenu2.add_command(label="잘라내기(T)")
fileMenu2.add_command(label="복사(C)", command=lambda : editFile(1))
fileMenu2.add_command(label="붙여넣기(P)", command=lambda : editFile(2))
fileMenu2.add_command(label="삭제(L)", command=lambda : editFile(3))
fileMenu2.add_separator()
fileMenu2.add_command(label="찾기(F)")
fileMenu2.add_command(label="다음 찾기(N)")
fileMenu2.add_command(label="바꾸기(R)")
fileMenu2.add_command(label="이동(G)")
fileMenu2.add_separator()
fileMenu2.add_command(label="모두 선택(A)")
fileMenu2.add_command(label="시간/날짜(D)")
window.mainloop()