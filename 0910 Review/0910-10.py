#이미지 출력
from tkinter import *
window=Tk()

#1번 이미지 파일 준비
photo=PhotoImage(file="gif/dog.gif")
#2번 Label()옵션에서 image 속성을 지정하여 글자대신 이미지 사용
label_img=Label(window, image=photo)
#3번 pack()함수를 호출하여 화면에 디스플레이
label_img.pack(side=LEFT);
photo2=PhotoImage(file="gif/dog2.gif")
label_img2=Label(window, image=photo2)
label_img2.pack(side=LEFT);


window.mainloop()

#photoImage는 gif파일만 지원한다.

