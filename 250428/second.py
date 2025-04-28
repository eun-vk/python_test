#입력


"""
입력을 몇가지 변수에 담아서 
f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요. 
"""

##형변환
#a= input("아무거나 입력해주세요.")
#print(type(a))
#b = int(a) #문자를 숫자로 
#print(type(b))
#
#a= 1
#print(type(str(a)))

#s= 'weniv CEO licat'
#print(s.lower())
#print(s.upper())
#
#print(s.find("weniv"))
#print(s.find("licat"))
#
#print(s.count("i"))
#
#s2= s.replace("CEO","DFE")
#print(s2)
#
#s3 = "wenive-corp"
#s4, s5 = s3.split("-")
#
#print(s4, s5)


#print("키, 몸무게, 성별, 나이, 이름을 입력해주세요.")
#info = input()
#a, b, c, d, e = info.split(" ")
#print("키=",a)
#print("몸무게=",b)
#print("성별=",c)
#print("나이=",d)
#print("이름=",e)
#print(f"{e*3}")
#s20= ["modu", "labs", "good"]
#print("-", join(s20))
#name = 'licat'
#age = 29
#
#print('제 이름은 {}이고, 나이는 {}살입니다.' format(name, age))
#print(f'제 이름은 {name}이고, 나이는 {age}입니다.')
#
#print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
#print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
#print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
#print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
#print("Backslash: \\") # 백슬래시를 출력합니다.

#bool 타입
a = 1
b = 0
c = -1
d ="okay"
f ="" 
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(f))

result = 5+3
print(result)

result = 3+ 2.5
print(result) 

print(11/2)
print(10/2)
print(type(10/2))
print(11//2)