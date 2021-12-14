#클래스 정의 부분
class car :
    color=""
    speed=0

    def __init__(self):
        self.color="빨강"
        self.speed=0
        
    def upspeed(self, value) :
        self.speed+=value
        
    def downspeed(self, value):
        self.speed-=value
        
#메인 코드 부분
mycar1=car()
mycar2=car()

print("자동차1의 색상은 %s이며, 현재속도는 %d km입니다."
      %(mycar1.color, mycar1.speed))
print("자동차2의 색상은 %s이며, 현재속도는 %d km입니다."
      %(mycar2.color, mycar2.speed))
