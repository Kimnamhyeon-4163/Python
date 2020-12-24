"""
날짜 : 2020/12/23
이름 : 김남현
내용 : 파이썬 클래스 실습하기

"""
from Ch05.sub1.Account import Account
from Ch05.sub1.Calc import Calc
from Ch05.sub1.StockAccount import StockAccount
# Account 객체 생성
kb = Account('국민은행', '101-12-1234', '김유신', 10000)
kb.deposit(20000)
kb.withdrow(5000)
kb.show()

wr = Account('우리은행', '101-11-1111', '김춘추', 30000)

wr.deposit(20000)
wr.withdrow(7000)
wr.show()

# Calc 객체 생성
cal = Calc()
r1 = cal.plus(2, 3)
r2 = cal.minus(2, 3)
r3 = cal.multi(2, 3)
r4 = cal.div(4, 2)

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)


# 클래스 상속

kium = StockAccount('키움증권', '101-123-12345', '홍길동', 50000, '삼성전자', 1000, 10)
kium.buy(1000, 10)
kium.show()

