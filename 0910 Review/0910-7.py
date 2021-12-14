##클래스 정의 부분
class car:
    color=""
    speed=0

    def __init__(self, value1, value2):
        self.color=value1
        self.speed=value2
        
    def upSpeed(self, value):
        self.speed+=value
    def downSpeed(self, value):
        self.speed-=value

#메인 코드 부분
mycar1=car("빨강", 30)
mycar2=car("파랑", 60)

print("자동차1의 생상은 %s이며, 현재속도는 %d km입니다." %(mycar1.color, mycar1.speed))
print("자동차2의 생상은 %s이며, 현재속도는 %d km입니다." %(mycar2.color, mycar2.speed))
