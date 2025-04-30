
'''a, b, c = input().split()
a, b, c = int(a), int(b), int(c)


if a == b == c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+c*100)
else:
    print(((a if a>b else b) if ((a if a>b else b)>c) else c)*100 )


if a == b == c:
    price = 1000 + a *1000
elif a == b:
    prics = 1000+ a *100
elif a == c:
    prics = 1000+ a *100
elif c == b:
    prics = 1000+ c *100

else:
    price = 0 #출력할 때 모두 참이 아니면 price 의 값이 없으니까 임의로 price의 값을 0으로 둔다. (값이 없으면 오류가 뜨니까.)
if a != b and b != C and a != c :
    temp = a
    if b >temp:
        temp = b
    if c > temp:
        temp = c 
    price = temp *100

print(f"상금: {price}원")'''

'''z = [1, [2], 3] in [2] #[1, [2], 3]가 [2]에 있니?

a = input()
print(f"{a}??!")


y = int(input())


print(s)'''
 

'''test = [13, 56, ["apple", ["banana", ["peach"]], ["c", "d"]]]
print(len(test))

t2 = [1, 2, 3, [4, 5, [3,31]],1]
print(t2[3][2])  #[3,31] 추출

#수정
t2[0] = 5 #tw에 있는 0번째 값을 5로 바꾼다. 

t3 = [5, 4, 3, [2, 1]]
[1,2,3,[4,5]]'''

t3 = [5, 4, 3, [2, 1]]
t3[0] = 1
t3[1] = 2
t3[3] = [4, 5]
print(t3)


t4 = []
t4.append() # append는 리스트 뒤에 붙는다.
t4.clear() # 리스트 안 데이터 삭제 
t4.remove() #리스트 안에서 특정 값을 지운다. 
t4.sort() #오름차순 정렬 

#리스트 만들 때 방법 
a = []
b = list() #형변환이 필요할 때 

t4.pop() #리스트의 맨 오른쪽에 있는 값을 추출 후 
#마지막으로 입력된 데이터가 첫 번째로 삭제됨 -> last in first out  
