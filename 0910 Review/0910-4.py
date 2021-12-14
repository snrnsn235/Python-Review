##클래스 선언
class car :
    speed=0

    def upspeed(self, value):
        self.speed=self.speed+value
    def downspeed(self, value):
        self.speed=self.speed-value

class sedan(car) :
    seatnum=0

    def getseatnum(self):
        return self.seatnum
class truck(car) :
    capacity = 0
    def getcapacity(self):
        return self.capacity

#변수선언
sedan1, truck1 = None, None

#메인 코드 부분
sedan1=sedan()
truck1=truck()

sedan1.upspeed(100)
truck1.upspeed(80)

sedan1.seatnum=5
truck1.capacity=50

print("승용차의 속도는 %dkm, 좌석수는 %d입니다." %(sedan1.speed, sedan1.getseatnum() ))
print("트럭의 속도는 %dkm, 총중량은 %d톤입니다." %(truck1.speed, truck1.getcapacity() ))
