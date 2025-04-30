#문제1 : 인사하기 
name = input("이름을 입력해주세요.")
print(f"안녕하세요,{name}님!")

#문제2 : 에코 프로그램 
a = input()
s = a+a+a
print(s)

#문제3 : 나이 계산하기 
birth = int(input("출생년도를 입력해주세요."))
age = 2025-birth
print(f"당신의 나이는 {age}세 입니다.")

#문제4: 원 넓이 계산 
a = int(input("반지름을 입력하세요."))
b = 3.14
s = a*a*b
print(s)

#문제5: 여행 거리 계산 
a, b = map(int, input("시속과 시간을 입력하세요.").split())
c = a * b
print(f"총 이동 거리: {c}")

#문제6: 문장 합치기 
a, b = input().split()
print(a +' '+b )

#문제7: 인치- 센티미터 변환
a = int(input("인치를 입력해주세요."))
b = a * 2.54
print(b)

#팁 계산기 
a = int(input("식사금액을 입력해주세요."))
b = int(input("팁 비율을 입력해주세요."))

c = a *(b/100)
d = a + b

print(f"팁 금액: {c}원")
print(f"총 지불 금액: {d}원")

#문제9: BMI계산기 
cm = int(input("키를 입력해주세요."))
kg = int(input("몸무게를 입력해주세요."))
m = float(cm/100)
bmi = kg / (m*m)
print(f"BMI: {bmi:.2f}")

#문제10: 다중입력 
a = list(map(int, input().split()))
print(f"첫 번째 숫자 : {a[0]}")
print(f"마지막 숫자 : {a[-1]}")

#문제11: 변수교환
a, b = input().split()
print(f"교환 전: a = {a}, b = {b}\n교환 후: a = {b}, b = {a}")

#문제12: 문자열 정보 출력 
a = input("문자를 입력하세요")
s = len(a)
print(f"문자열 길이: {s}")
print(f"첫 글자:", a[0])
print(f"마지막 글자:", a[-1])

##문제13: 이니셜 만들기 
a, b = input("성과 이름을 입력해주세요.").split()
print(f"이니셜: {a[0].upper()}.{b[0].upper()}.")

#문제14: 소수점 자릿수 
a = float(input())
print(f"{a:.2f}")

#문제15: 나이 구간 판별
age = int(input("나이를 입력하세요."))
if age>= 65:
    print("노년")
elif age >= 35:
    print("중장년")
elif age >= 19:
    print("청년")
else:
    print("미성년자")

##문제16: 문자열 분석 
a = input()
b = a.count(' ')
c = ""
d = len(a)

#문제17: 참/거짓 변환
a = input()
a = bool()
print(a)

#문제18: 홀짝 판별 
a = int(input("숫자를 입력하세요."))
if a%2 ==0:
    print("f{a}은(는) 짝수입니다.")
else: 
    print(f"{a}은(는) 홀수입니다.")

##문제19: 문자열 분할 
a = input()
s = ' '.join(a.split(","))
print(s)

#문제20: 온도 단위 변환기 
a = float(input("온도를 입력해주세요."))
b = input("온도 단위를 입력해주세요.")
b = "C" or "F"
if b == "C":
    print(f"{a}ºC는 {a*9/5+32}ºF입니다.")
else:
    print(f"{a}ºF는 {(a-32)*5/9}ºC입니다.")


