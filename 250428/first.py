#정수 
a = 10
b = 20
c = 0
d = -40
print(type(a), type(b), type(c), type(d)) #',' 띄어쓰기 역할 
print(int(9.53333))
#실수 
number1 = 3.12
number2 = -0.12
print(type(number1), type(number2))

#무한대 
x= float("inf")
y= float("-inf")

#문자열
str1 = "abcd"
str2 = 'adcd'

str3 = '''
오늘은 4월 28일입니다. 
5월이 머지 않았네요. 
'''
print(type(str3))
print(str3)

#문자열 이어붙이기 
str6 = "modu"
str7 = "dfdg"
print(str6+str7)

# 개인정보 출력해보기 

first_name = '최'
name = '은빈'
print(first_name + name)

n1 = '050606'
n2 = '4562849'
print(n1+'-'+n2)

email_1 = 'ekfjdo34'
email_2 = 'naver.com'
print(email_1+'@'+email_2)

str10 = str1 * 10 
test2 = "30"

print(str10)

# print(str1 * test2) (X)
print(str10+"입니다"+"네네")


a="4"
b="28"

#기본방식 
print("오늘은"+a+"월" +b+"일입니다.")

# f-string
# f""
print(f"오늘은 {a}월 {b*10}일입니다.")

# 문자열 인덱싱 

s= "life is good" #0~11번째까지의 인덱스 
print(s[0]) #인덱싱 
print(s[3]) 
print(s[-1])


s = 'weniv CEO licat'
print(1,s[0:5])
print(2,s[6:])
print(3,s[:]) #=print(3,s)
print(5,s[::2])

# 테스트 
## ip address = 172.100.200.100

'''
1.ip address문자열을 슬라이싱 기법을 활용해 변수에 담아 출력 
2.a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다. 
3.step을 활용해서 172100200100이 나오게 하기 
'''


s = "ip address = 172.100.200.100"
print(s[0:11])
a= s[13:16]
b= s[17:20]
c= s[21:24]
d= s[25:28]
print(f"{a}{b}{c}{d}")









