##리스트 []##
#지하철 칸별로 10명 20명 30명
'''
subway1=10
subway2=20
subway3=30

subway=[10, 20, 30]
print(subway)

subway=["유재석", "조세호", "박명수"]
print(subway)

#조세호씨가 몇번째칸에 있는가?
print(subway.index("조세호"))
#하하씨가 다음 정류장에서 탔다
subway.append("하하") #맨뒤에 붙일수 있
print(subway)
#정현돈씨를 유재석/조세호 사이에 넣어보자
subway.insert(1, "정형돈")
print(subway)
#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

#같은 이림의 사람이 몇명있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
'''
##사전##
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print()
print(cabinet.get(3))
#print(cabinet[5]) 오류가 나서 종료가 되지만
print(cabinet.get(5)) #get을 사용하면 오류가 나지 않고 none만 뜨고 계속 실행이됨
print(cabinet.get(5, "사용가능"))
print("hi")
print()
print(3 in cabinet) #True
print(5 in cabinet) #False
cabinet = {"A-3" :"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print()
#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)
print()
#간 손님
del cabinet["A-3"]
print(cabinet)
print()
#key들만 출력
print(cabinet.keys())
#value들만 출력
print(cabinet.values())
#key, value쌍으로 출력하려면
print(cabinet.items())
print()
#목욕탕 폐점
cabinet.clear()
print(cabinet)






































