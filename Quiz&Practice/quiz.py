#퀴즈1>
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")


#퀴즈2> 당신은 최근에 코딩 스터디모임을 새로 만들었다.
#월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했다.
#아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
#조것1 : 랜덤으로 날짜를 뽑아야 함
#조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
#조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

#퀴즈3>사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
'''예)http://naver.com
규칙1 : http://부분은 제외 ->naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내'e'갯수+"!"로 구성
예)생성된 비밀번호 : nav51!'''

site = "http://naver.com"
x=site.replace("http://", "")
print(x)
#print("규칙1 : " + site[7:])
#print("규칙1-1: " + site.replace("http://", ""))
x = x[:x.index(".")] #site[0:5] ->0~5직전까지 
print(x)
password = x[:3] + str(len(x)) + str(x.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(site, password))
