print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print()
print()
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
print()
print()
#참/거짓
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
print()
print()
# 변수
## 애완동물을 소개해 주세요
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 "+ name +"이예요")
print(name + " 는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name +" 는 어른일까요? " + str(is_adult))
print()
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3
### 변수는 중간에도 넣을수있다
print("우리집 " + animal + "의 이름은 "+ name +"이예요")
hobby = "공놀이"
##위에 문장까지는 취미가 낮잠이 되지만 밑에 문장부터는 공놀이가 된다.
#print(name + " 는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
## ','를 사용하면 윗줄처럼 str을 안넣어도 됨
print(name , "는 ",age,"살이며, ",hobby,"을(를) 아주 좋아해요")
print(name +" 는 어른일까요? " + str(is_adult))
print()
##주석 # 혹은 (''')를 사용하면된다
print()
##연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)
print()
print(2**3) #2의 3승 8
print(5%3) #2
print(10%3)
print(5//3) #몫 1
print(10//3) #몫 3
print()
print(10>3)
print(4 >= 7)
print(10<3)
print(5 <= 5)
print(3==3)
print(4 == 2)
print (3 + 4 ==7)
print()
print(1 != 3)
print(not (1 != 3))
print((3>0) and (3<5))
print((3>0) & (3<5))
print()
print((3>0) or (3>5)) #true
print((3>0) | (3>5)) #true
print(5 > 4 >3)
print(5>4>7)
print()
print()
##수식
print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number + 2
print(number)
number+=2 #18
print(number)
number *=2
print(number)
number /= 2
print(number)
number -= 2
print(number)
print()

number %=5
print(number)


##절대값
print(abs(-5))
print(pow(4, 2)) #4를 두번곱한 값 16
print(max(5,12)) #두 값중 최대값을 출력
print(min(5,12)) #두 값중 최소값을 출력 
print(round(3.14)) #3.14를 반올림한 값이 출력
print(round(4.99)) 
print()
print(floor(4.99))





