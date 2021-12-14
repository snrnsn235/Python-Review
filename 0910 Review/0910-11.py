from tkinter import *
window=Tk()
#command 옵션에 quit명령을 줬으므로 버튼을 클릭하면 파이썬 IDLE이 닫힘
button1=Button(window, text="파이썬 종료", fg="red", command=quit)
button1.pack()
window.mainloop()

