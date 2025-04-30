

a = 10
b = 20

if a>10:
    print("good")
elif b ==20: #if가 거짓일 때 elif값을 출력함. 
    print("20입니다.") #파이썬은 위에서 아래로 읽는다. 위의 값이 참이면 아래 값은 보지 않는다. 
elif a == 10:
    print("10입니다.")

# split()활용 , a,b 변수 활용, 키와 몸무게 입력, 
print("키와 몸무게를 입력해주세요.")
a, b = map(int,input().split())
if 130<= a <150:
    print("a")
elif a < 170:
    print("b")
elif a < 180:
    print("c")
else: 
    print("d")


a, b, c = map(int, input().split())
if a%2 ==0:
    print(a)

if b%2 ==0:
    print(b)

if c%2 ==0:
    print(c)

a,b,c = map(int, input().split())

if a%2 ==0:
    print("even")
else:
    print("odd")

if b%2 ==0:
    print("even")
else:
    print("odd")

if c%2 ==0:
    print("even")
else:
    print("odd")


a = int(input("점수를 입력해주세요"))

if a <60:
    print("F")
elif a <70:
    print("D")
elif a <80:
    print("C")
elif a <90:
    print("B")
else:
    print("A")


a = input()

if a =="A":
    print("best!!!")
elif a =="B":
    print("good!!")
elif a =="C":
    print("run!")
elif a =="D":
    print("slowly~")
else:
    print("what?")


m = int(input())

season = (m % 12)//3 

if season == 0: 
    print("winter")
elif season ==1:
    print("spring")
elif season ==2:
    print("summer")
else: 
    print("fall")


a, b, c = map(int, input().split())
 
if a == 100 and b>=200:
    print("a")
elif b ==1:
    print("b")
else:
    print("c")





    