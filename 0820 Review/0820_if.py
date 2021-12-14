##if문##
a=99
if a<100:
    print("100보다 작군요.")

print()
a=200
if a<100:
    print("100보다 작군요") #들여쓰기를 하지 않아 실행하지 않아야 할 5행까지 실행됨
print("거짓이므로 이 문장은 안 보이겠죠?")
print("프로그램 끝")
print()

a=200
if a<100:
    print("100보다 작군요")
    print("거짓이므로 이 문장은 안 보이겠죠?") #들여쓰기를 해서 오류를 수정함 
print("프로그램 끝")


##if-else##
a=200
if a<100:
    print("100보다 작군요.")
else :
    print("100보다 크군요.")
print()
a=int(input("정수를 입력하세요 : "))
if a%2== 0:
    print("짝수를 입력했군요.")
else :
    print("홀수를 입력했군요.")
print()

##if문안에 또다른 if문##
a=int(input("정수를 입력하세요 : "))
if a>50:
    if a<100:
        print("50보다 크고 100보다 작군요.")
    else:
        print("와~100보다 크군요.")
else :
    print("에고~50보다 작군요.")
print()
score=int(input("점수를 입력하세요 : "))
if score>=90:
    print("A")
else:
    if score>=80:
        print("B")
    else:
        if score>=70:
            print("C")
        else:
            if score>=60:
                print("D")
            else:
                print("F")
print()

score=int(input("점수를 입력하세요 : "))
if score==100:
    print("A+")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
print()

#변수 선언 부분
a,b,ch =0,0," "
#메인(main)코드 부분
a=int(input("첫번째 수를 입력하세요 : "))
ch=input("계산할 연산자를 입력하세요 : ")
b=int(input("두번째 수를 입력하세요 : "))
if ch=="+":
    print("%d+%d=%d 입니다." %(a,b,a+b))
elif ch=="-":
    print("%d-%d=%d 입니다."%(a,b,a-b))
elif ch=="*":
    print("%d*%d=%d 입니다."%(a,b,a*b))    
elif ch=="/":
    print("%d/%d=%d 입니다."%(a,b,a/b))
elif ch=="//":
    print("%d//%d=%d 입니다."%(a,b,a//b))
elif ch=="**":
    print("%d**%d=%d 입니다."%(a,b,a**b))
else:
    print("알 수 없는 연산자입니다.")
print()
##if문 응용##
fruit=['사과', '배', '딸기', '포도']
print(fruit)
fruit.append('귤')#뒤에 추가시키는것 
print(fruit)
if '딸기' in fruit: #if 항목 in 리스트 : 리스트 안에 항목이 있으면 True
    print("딸기가 있네요!")
print()

import random
numbers=[] #랜덤하게 숫자가 나옴
for num in range(0, 10): #num이 0~9까지 반복해서 나옴
    numbers.append(random.randrange(0,10)) #시작부터 끝-1까지 숫자 중에서 임의의 숫자를 하나 반환
    #0~9까지 숫자 중에서 임의의 숫자를 반환
print("생성된 리스트", numbers)
for num in range(0, 10):
    if num not in numbers:
        print("%d 숫자는 리스트에 없네요." %num)
print()





















    

        
