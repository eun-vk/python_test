# 한줄 주석 #앞에 있는 것은 코드로 인식 
# ctrl + /

'''
다중 주석 
'''
#변수 
name = "김치찌개"  #변수 = 값 / name 코드가 끝나면 사라진다. 
food = "김치볶음밥"
# 변수이름은 있어야 한다. 

money = "1000원"
student = "홍길동"
book_name = "나는 메트로폴리탄 미술관의 경비원입니다."
brand = "샤넬"
make = "한국"

print(money, student, book_name, brand, make)
a= 10
b= 20
print(a,"+",a,"=", b)

PI=3.14
PI= 3.14

print(type(PI))
print(type(name))

j = 10
j = 10.5222222222222

print(f"j의 값은 {j:.sf}")
print(f"j의 값은 {j:.2f}") #j의 값을 소수점 둘째자리 까지 표현한다. 
money = 1000000000000000
print(f"{money:,} 원 갖고 싶어요") # 3자리 수로 콤마(,)를 찍어서 출력 

