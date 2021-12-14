from tkinter import *
window=Tk()
##라벨은 문자를 표현할 수 있는 위젯
#형식은 Label(부모윈도우, 옵션)
#부모 윈도우로 window를 지정, 베이스 윈도우에 라벨이 출력
label1 = Label(window, text = "SWEDU~~ Python을")
label2 = Label(window, text = "열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text = "화이팅", bg="magenta", width=20,
               height=5, anchor=SE)
#anchor는 위젯이 어느 위치에 자리 잡을 지 지정, SE는 남동쪽
#N, NE, E, SE, S, SW, W, NW, CENTER
# pack()함수를 호출하여 화면에 디스플레이됨
label1.pack()
label2.pack()
label3.pack()

window.mainloop()

##Hex, #000000(RGB) - black, #ffffff - white #dddddd, 222222 - gray
##ff0000 - red, 0000ff - blue, 00ff00 - green



