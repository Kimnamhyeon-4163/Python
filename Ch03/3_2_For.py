"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 반복문 For 실습하기

"""

# 리스트를 이용한 for
for num in [1, 2, 3]:
    print('num :', num)

people = ['김유신','김춘추','장보고','강감찬','이순신']
for person in people:
    print(person)
# 튜플을 이용한 for
for num in (1, 2, 3):
    print('튜플 num :', num)

countries = ('한국','미국','일본','중국','호주')
for country in countries:
    print(country)
# range() 함수를 이용한 for
for i in range(5):
    print('i :', i)

for k in range(11, 20):
    print('k :',k)


# 1부터 10까지 합
sum1 = 0

for k in range(11):
    sum1 += k

print('1부터 10까지 합 : ', sum1)

# 1부터 10까지 짝수합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k

print('1부터 10까지 짝수합 : ', sum2)

# 이중 for
for a in range(3):
    print('-------')
    print('a : ', a)
    for b in range(5):
        print('b : ', b)

# 구구단
for a in range(2, 10):
    print(a, '단 출력')
    for b in range(1, 10):
        c = a * b
        print('%d x %d = %d' % (a, b, c))

# 별삼각형
for a in range(10):
    for b in range(a+1):
        print('★', end='')

    print()


for i in range(11):
    print('☆'*i)

for a in range(10):
    for b in range(10-a):
        print('★', end='')
    print()

for a in range(10, 0, -1):
    for b in range(a):
        print('★', end='')
    print()