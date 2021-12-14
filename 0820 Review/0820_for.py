##for문##
for i in range(0,3,1) :#0-초기값 3-조건식 1-증감식 이 부분을 반복
    print("안녕하세요? for문을 공부중입니다. ^^")
print()
for i in [0,1,2] :#0-초기값 3-조건식 1-증감식 이 부분을 반복
    print("안녕하세요? for문을 공부중입니다. ^^")
#range()함수는 지정된 범위의 값을 반환
#range(0,3,1)은 [0,1,2]와 같음
print()
for i in range(0,3,1) :#0-초기값 3-조건식 1-증감식 이 부분을 반복
    print("%d : 안녕하세요? for문을 공부중입니다. ^^"% i)
print()
for i in range(2,-1,-1) :
    print("%d : 안녕하세요? for문을 공부중입니다. ^^"% i)
print()
for i in range(1,6,1):
    print("%d" % i, end=" ") #end=""는 뒤에 띄어쓰기를 적용한것


i=0
for i in range(1,11,1):
    hap=hap+i #에러발생
    print("1에서 10까지의 합 : %d" %hap)


i, hap = 0, 0

for i in range(1, 11, 1):
    hap=hap+i #hap=0+1 hap=1+2 hap=3+3 ....hap=45+10
    print("1에서 10까지의 합 : %d" %hap)

i,hap=0,0
for i in range(1, 11, 2):
    hap+=i
    print("1에서 10까지 홀수의 합 : %d" %hap)


i,hap = 0,0
num=0

num=int(input("값 입력 : "))

for i in range(1, num+1, 1):
    hap+=i
print("1에서 %d까지 합 : %d" %(num, hap))

i,hap=0,0
num1,num2,num3=0,0,0

num1=int(input("시작값 입력 : "))
num2=int(input("끝값 입력 : "))
num3=int(input("증가값 입력 : "))

for i in range(num1, num2+1, num3):
    hap+=i
print("%d에서 %d까지 %d씩 증가함 값의 합 : %d" %(num1, num2, num3, hap))


print()
i,dan=0,0
dan=int(input("몇 단? "))
for i in range(1,10,1):
    print("%d X %d = %2d" %(dan, i, dan*i))
print()
##for문 안에 for문##
for i in range(0,3,1):
    for k in range(0,2,1):
        print("파이썬은 꿀잼입니다.^^ (i걊:%d, k값:%d)" %(i, k))
#중첩 for문의 실행 횟수는 '바깥 for문 반복 횟수 X 안쪽 for문 반복 횟수' 



print()
i,k=0,0
for i in range(2,10,1):
    for k in range(1,11,1):
        print("%d X %d = %2d" %(i, k, i*k))
    print("")
print()
#변수선언부분#
i,k,guguLine=0,0,""
#메인(main)코드 부분#
for i in range(2,10):
    guguLine=guguLine+("# %d단 # " %i)
    
print(guguLine)

for i in range(1,10):
    guguLine=""
    for k in range(2,10):
        guguLine=guguLine+str("%2dX%2d=%2d" %(k, i, k*i))
    print(guguLine)
    
   



















