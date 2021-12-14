#thinter는 GUI 관련 모듈을 제공해주는 표준 윈도우 라이브러리
#윈도우 창을 출력할 때 반드시 입력해야 함
from tkinter import*
#Tk()는 기본이 되는 윈도우를 반환, 루트 윈도우 또는 베이스 윈도우라고 함
window = Tk()

#윈도우 창조절하기
#4행 윈도우 창에 제목 표시
#5행에서는 윈도우 창의 초기 크기를 400X100으로 지정
#6행은 가로 세로의 크기가 변경되지 않도록 설정
window.title("윈도우 창 연습")
window.geometry("400x100")
#TRUE 대신 1을 넣어도 된다.
window.resizable(width=FALSE, height=FALSE)
#화면을 구성하고 처리
#윈도우 창에 키보드 누르기, 마우스 클릭 등 다양한 이벤트를 처리 
window.mainloop()
