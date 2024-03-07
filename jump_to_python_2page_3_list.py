#리스트
odd = [1,3,5,7,9] #리스트명 = [요소1, 요소2, 요소3]
a = list() #비어있는 리스트
#리스트의 인덱싱
a = [1,2,3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[-1][1]) # a리스트 안에 있는 리스트 중에 b
#삼중 리스트
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[-1][-1][0])
#리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
a = "12345"
print(a[0:2])
#리스트 더하기
a = [1,2,3]
b = [4,5,6]
print(a+b)
#리스트 반복하기
a = [1,2,3]
print(a*3)
#리스트 길이 구하기
print(len(a))
#리스트 수정과 삭제
a = [1,2,3]
print(a)
a[2] = 4
print(a)
del a[1]  #삭제
print(a)
