##클래스 선언
class car:
    name=""
    speed=0

    def __init__(self,name,speed): #생성자
        self.name=name
        self.speed=speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed
#변수 선언
car1, car2 = None, None
#메인 코드 부분
car1=car("아우디",0)
car2=car("벤츠", 30)

print("%s의 현재 속도는 %d입니다." %(car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다." %(car2.getName(), car2.getSpeed())) 
