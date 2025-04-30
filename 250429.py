 # and 연산 
 ## 다른 언어에서는 
 # a&& b 
a = True
b = True 
c = a and b 
d = 10 > 5 and 10 < 5 #d = True and False 
print(d)
f = 10 >= 10 or False #앞에 이미 True가 나왔기 때문에 뒤에 값이 무엇이든 True가 성립 
f = False and True and True # 0 1 1
print(f)
f2 = (False or True) and True 
print(f2) 
f3 = ((False or True) and True) #가독성이 좋지 않으니 지양해야 함. 
print(f2)
a = 10
b = 20
c = a!=b #다르니? 라고 물어보는 것 =True(다르다) 
c = not a!=b # 다르지 않아. 그렇지? =False
 

print("a,b,c를 입력하세요.")
a = int(input())
b = int(input())
c = int(input())
s = a >30 or b <20 and c <12
print(s)

 ##항은 3개 이상 and, or은 마음대로 연결하여 결과 출력 


#멤버연산 
st = "modulabs is good"
sta = "good" in st
a, b, c = input().split()
# split 
a = "123456-1122335" 
c,d = a.split("-")
s = input("a, b, c를 공백으로 구분해서 입력하세요.")
a, b, c = s.split()
a = int(a)
b = int(b)
c = int(c)
su = a + b + c
av = su / 3
print(su, f"{av:.2f}")
# 조건문 
age = 20 
height = 130
if age >= 18 or height >= 150:
    print("성인입니다.")
else: 
    print("성인이 아닙니다.")
"""한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)"""

y, m, d = input().split()
y = int(y)
m = int(m)
d = int(d)

if y%2 == 0:
   print("짝수년도에 태어났습니다.")
else:
   print("홀수년도에 태어났습니다.")

yyyy, mm, dd = input().split()
yyyy, mm, dd = int(yyyy), int(mm), int(dd)

if yyyy % 2 ==0:
    print("짝수년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")
