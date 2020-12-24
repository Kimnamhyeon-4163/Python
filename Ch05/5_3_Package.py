"""
날짜 : 2020/12/23
이름 : 김남현
내용 : 파이썬 패키지 실습하기
"""

from Ch05.sub3.Account import Account
from Ch05.sub3.calc import *


nh = Account('농협', '111-12-1212', '이순신', 10000)
nh.deposit(20000)
nh.withdrow(5000)
nh.show()

r1 = plus(1, 2)
r2 = minus(1, 2)
r3 = multi(2, 3)
r4 = div(4, 2)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)