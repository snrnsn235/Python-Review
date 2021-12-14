'''
##리스트##

a,b,c,d = 0, 0, 0, 0 #abcd를 각각 '0'으로 선언
hap = 0 #hap을 '0'으로 선언

a=int(input("1번째 숫자 : "))
b=int(input("2번째 숫자 : "))
c=int(input("3번째 숫자 : "))
d=int(input("4번째 숫자 : "))

hap=a+b+c+d #hap은 a+b+c+d이라고 선언
print("합계==>%d" % hap)
print()

##위의 코드를 수정##
aa=[0,0,0,0]
hap = 0

aa[0] = int(input("1번째 숫자를 입력하세요 : "))
aa[1] = int(input("2번째 숫자를 입력하세요 : "))
aa[2] = int(input("3번째 숫자를 입력하세요 : "))
aa[3] = int(input("4번째 숫자를 입력하세요 : "))

hap = aa[0]+aa[1]+aa[2]+aa[3]
print("합계 : %d" % hap)
print()
'''
##빈 리스트와 리스트의 추가
#비어있는 리스트를 만들고 '리스트이름.append(값)'함수로 리스트에 하나씩 추가
'''
aa=[]
aa.append(123)
aa.append(456)
aa.append(789)
aa.append(10)
print(aa)
print()
'''
'''
aa=[]
for i in range(0, 100):
    aa.append(0)
    
len(aa)
'''
'''
aa=[]
for i in range(0, 4, 1):
    aa.append(0)
hap=0

for i in range(0, 4, 1):
    aa[i]=int(input(str(i+1)+ "번째 숫자 : "))

hap=aa[0]+aa[1]+aa[2]+aa[3]
print("합계==> %d" %hap)
print()
'''
'''
aa=[]
bb=[]
value=0

for i in range(0, 100):
    aa.append(value)#aa[0]=0, aa[1]=2.....aa[99]=198
    value+=2

for i in range(0, 100):
    bb.append(aa[99-i])#aa[99-0]=aa[99]=198 => bb[0]=198...aa[99-99]=aa[0]=0 => bb[99]=0

print("bb[0]은 %d, bb[99]는 %d 입력됨" %(bb[0],bb[99]))
'''
'''
aa=[10,20,30,40]
print("aa[-1]은 %d, aa[-2]는 %d" %(aa[-3],aa[-4]))

aa=[10,20,30,40]
aa[0:3]
aa[2:4]
aa[2:]
aa[:4]

'''

list1=[]
list2=[]
value=1
for i in range(0,3,1):
    for k in range(0,4,1):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]

for i in range(0,3,1):
    for k in range(0,4,1):
        print("%5d" % list2[i][k], end="")
    print("")


































