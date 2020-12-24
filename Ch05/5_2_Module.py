"""
날짜 : 2020/12/23
이름 : 김남현
내용 : 파이썬 모듈 실습하기
"""
import Ch05.sub2.calc
import Ch05.sub2.calc as cal
r1 = Ch05.sub2.calc.plus(1, 2)
r2 = cal.minus(1, 2)
r3 = cal.multi(2, 3)
r4 = cal.div(4, 2)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)