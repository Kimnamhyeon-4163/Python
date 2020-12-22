"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 함수 고급 실습하기
"""

# 기본값 매개변수
def hello(name='홍길동', old=20):
    print('---------------------')
    print('이름은 %s 입니다.' % name)
    print('나이는 %d 입니다.' % old)


hello()
hello('김춘추')
hello('김유신', 25)

# 가변 매개변수
def total(*param):
    tot = 0
    for k in param:
        tot += k

    return tot

r1 = total(1)
r2 = total(1, 2, 3)
r3 = total(1, 2, 3, 4, 5)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)

# 여러개의 값을 반환하는 함수
def sum_and_mul(x, y):
    z1 = x + y
    z2 = x * y

    return z1, z2

rs1, rs2 = sum_and_mul(1, 2)
rs3, rs4 = sum_and_mul(2, 3)

print('rs1 : ', rs1)
print('rs2 : ', rs2)
print('rs3 : ', rs3)
print('rs4 : ', rs4)




# 함수의 지역변수, 전역변수
# 함수를 변수에 저장해서 호출하기