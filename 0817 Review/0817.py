from random import *
'''
print(random()) # 0.0~1.0미만의 임의의 값을 생성
print(random() *10) #0.0~10.0미만의 임의의 값을 생성
print(int(random()*10)) #0~10미만의 임의의 값을 생성(int를 넣어줌으로써 소수점이 사라짐)
print(int(random()*10))
print(int(random()*10))
print()
print(int(random()*10)+1) #1~10미만의 임의의 값을 생성 
print(int(random()*10)+1) #1~10미만의 임의의 값을 생성 
print(int(random()*10)+1) #1~10미만의 임의의 값을 생성 
print(int(random()*10)+1) #1~10미만의 임의의 값을 생성 
print(int(random()*10)+1) #1~10미만의 임의의 값을 생성 
print()
print(int(random() * 45) +1 )
print(int(random() * 45) +1 )
print(int(random() * 45) +1 )
print(int(random() * 45) +1 )
print(int(random() * 45) +1 )
print()
print(randrange(1, 46)) #1~45미만의 임의의 값 생성 
print(randrange(1, 46)) #1~45미만의 임의의 값 생성
print(randrange(1, 46)) #1~45미만의 임의의 값 생성
print(randrange(1, 46)) #1~45미만의 임의의 값 생성
print(randrange(1, 46)) #1~45미만의 임의의 값 생성
print(randrange(1, 46)) #1~45미만의 임의의 값 생성 
print()
print(randint(1,45))##1~45이하의 임의의 값 생성
print(randint(1,45))##1~45이하의 임의의 값 생성
print(randint(1,45))##1~45이하의 임의의 값 생성
print(randint(1,45))##1~45이하의 임의의 값 생성
print(randint(1,45))##1~45이하의 임의의 값 생성

##문자열##

sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

##슬라이싱##
jumin = "920304-1234567"

print("성별 : " + jumin[7]) #0부터 시작 
print("연 : " + jumin[0:2]) #0번째 부터 2번째자리 전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) #처음부터 6직전까지 
print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지 
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

##문자열 처리 함수##
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print()
index=python.index("n")
print(index)
index=python.index("n", index+1)
print(index)
print()
print(python.find("Java")) #값이 -1이되고 다음입력값인 hi가 출력이되나
#print(python.index("Java"))#index일때는 에러가 뜨고 프로그램을 종료해버
print("hi")
print()
print(python.count("n")) #몇번나오는지 알려줌

'''
##문자열포맷##
print("a" + "b")
print("a","b")
print()
##다른방법들
#방법1
print("나는 %d살입니다." % 20) #d는 정수값만 가능
print("나는 %s을 좋아해요." % "파이썬")#s는 string
print("Apple은 %c로 시작해요." %"A") # c는 한글자만 받는다는뜻 
print("나는 %s살입니다." % 20) #s는 정수값도 포함하므로 가능한 문제이다 
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
print()
#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {2}색을 좋아해요.".format("파란", "빨간", "노랑"))
print()
#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20)) #둘의 순서가 바뀌어도 괜찮음 
print()
#방법4
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
print()
##탈출 문자##
# \n:줄바꿈 
print("백문이 불여일견\n백견이 불여일타")
print()
#저는 "나도코딩"입니다.
#\", \' : 문장에서 따옴표 
print("저는 '나도코딩'입니다")
print('저는 "나도코딩"입니다')
print("저는 \"나도코딩\" 입니다")
print('저는 \'나도코딩\'입니다')
print()
# \\ : 문장 내에서 하나의 \로 바뀜
print("C:/Users/snrns/AppData/Local/Programs/Python/Python39/0817")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")





















