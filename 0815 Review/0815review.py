'''
print("반가워요~~파이썬 ^^")
print()
print()
a=100
b=50
result = a+b
print(a,"+",b ,"=", result)
result=a-b
print(a, "-", b, "=", result)
result=a*b
print(a, "*", b, "=", result)
result=a/b
print(a, "/", b, "=", result)
print()
print()
print()

a=int(input("첫 번째 숫자를 입력하세요 : " ))
b=int(input("두 번째 숫자를 입력하새요 : " ))
result = a+b
print(a,"+",b ,"=", result)
result=a-b
print(a, "-", b, "=", result)
result=a*b
print(a, "*", b, "=", result)
result=a/b
print(a, "/", b, "=", result)
print()
print()
print()'''

'''
#tkinter는 파이썬에서 GUI관련 모듈을 제공해주는 표준 윈도우 라이브러리
from tkinter import *

#Tk()는 기본이 되는 윈도우를 반환, 루트 윈도우, 베이스 윈도우라고함
window=Tk()
window.title("윈도우 창 연습")
window.geometry("400x100")
#가로와 세로의 크기가 변경되지 않도록 설정(FALSE는 변경되지 않도록, TRUE는 변경되도록)
window.resizable(width=FALSE, height=FALSE)
#이부분에서 화면을 구성하고 처리
window.mainloop()'''

'''
from tkinter import*

##변수선##
window=None
canvas=None

##함수##

##메인 코드##
window=Tk()
window.title("그림판 비슷한 프로그램")
#윈도우 안의 캔버스를 만들어
canvas=Canvas(window, height=300, width=300)
canvas.pack()
window.mainloop()'''

from tkinter import*

##변수선언##
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None # 선의 시작점(x1, y1)과 끝점(x2, y2)

##함수선언##
###마우스를 클릭할 때 작동하는 함수
#def는 함수를 선언하는 문장, mouseClick()이라는 함수를 만듦
def mouseClick(event) :
    global x1, y1, x2, y2 #global 뒤의 변수는 해당 변수들을 전역변수로 인정한다는 의미
    x1=event.x
    y1=event.y
###마우스를 드롭할 때 작동하는 함수
#mouseDrop()이라는 함수를 만듦    
def mouseDrop(event) :
    global x2, y2
    x2.event.x
    y2.event.y
#이 시점에 선이 그려짐
    canvas.create_line(x1,y1,x2,y2, width=5, fill="red")
#canvas.create_line(x1,y1,x2,y2)는 캔버스에서 시작, 끝점까지 선을 그려짐

##메인 코드##
window.title("그림판 비슷한 프로그램")
canvas=Canvas(window, height=300, width=300)
canvas.bind("<Button-1>", mouseClick)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()
window.mainloop()







