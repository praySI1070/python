# 파이썬에서 문자열 만들기
# "HEllo world"
# 'Python is fun'
# """Life is too short, you need python"""
# '''Life is too short, you need python'''
a = """Hello world"""
print(a)
#문자열에 작은따옴표 포함하기
food = "Python's favorite food is perl"
#작은 따옴표가 안에 들어가면 큰 따옴표 사용
#food = 'Python's favorite food is perl'
print(food)
#역슬레시 사용
food = 'Python\'s faverite food is perl'
print(food)
#여러 줄인 문자열을 변수에 
#개행 사용
multiline = "Life is too short\nYou need python"
print(multiline)
#연속된 따옴표 3개 사용
multiline = '''
Life is too short
You need python
'''
print(multiline)
#문자열 연산
#문자열 더해서 연결
head = "Python"
tail = " is fun!"
print(head + tail)
#문자열 곱하기
a = "Python"
print(a*2)
#응용 -> multistring.py cmd에서 실행
#문자열 길이
a = "test"
print(len(a))
#문자열 인덱싱과 슬라이싱
#인덱싱
a = "Life is too short, You need Python"
print(a[3])
print(a[-2])
#문자열 슬라이싱
print(a[0:4]) # 0 <= a < 4
#슬라이싱으로 문자열 나누기
a = "20240306Sunny"
date = a[:8]
weather = a[8:]
print(date,weather)
#Pithon -> Python으로 변환
a = "Pithon"
print(a[:1] + "y" + a[2:]) #문자열은 수정 불가하므로 이렇게 변경
#문자열 포매팅
print("I eat %d apples." % 3)
print("I eat %s apples." % 'five')
print("I ate %d apples. so I was sick for %s days." % (3,'five'))
# %o 8진수
# %x 16진수
# %% 문자 % 자체
#포맷 코드와 숫자 함꼐 사용하기
