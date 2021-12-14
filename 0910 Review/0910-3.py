##클래스 선언
class car:
    color:""#인스턴스
    speed=0 #인스턴스 변수
    count=0 #클래스변수

    def __init__(self):
        self.speed=0
        car.count+=1

#변수 선언
mycar1, mycar2 = None, None

#메인코드부분
mycar1=car()
mycar1.speed=30
print("자동차1의 현재속도는 %dkm, 생산된 자동차 숫자는 총 %d대 입니다."
%(mycar1.speed, car.count))
mycar2=car()
mycar2.speed=60
print("자동차2의 현재속도는 %dkm, 생산된 자동차 숫자는 총 %d대 입니다."
%(mycar2.speed, mycar2.count))
