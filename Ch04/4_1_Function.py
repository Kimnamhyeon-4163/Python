"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 함수 실습하기
"""

# 함수정의
def f(x):
    y = 2 * x + 3
    return y

# 함수호출
rs1 = f(1)
rs2 = f(2)
rs3 = f(3)

print('rs1 : ', rs1)
print('rs2 : ', rs2)
print('rs3 : ', rs3)

# 함수타입1 - 매개변수 O, 반환값 O
def f1(x, y):
    z = x + y
    return z

# 함수타입2 - 매개변수 X, 반환값 O
def f2():
    tot = 0
    for k in range(11):
        tot += k

    return tot

# 함수타입3 - 매개변수 O, 반환값 X
def f3(items):
    tot = 0
    for i in items:
        tot += i

    print('items 합 : ', tot)

# 함수타입4 - 매개변수 X, 반환값 X
def f4():
    for i in range(11):
        print('★'*i)


r1 = f1(1, 2)
r2 = f1(2, 3)

print('r1 : ', r1)
print('r2 : ', r2)

r3 = f2()
print('r3 : ', r3)

f3([1, 2, 3, 4, 5])
f3((6, 7, 8, 9, 10))

f4()