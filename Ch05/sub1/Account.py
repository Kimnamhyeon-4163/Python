# 클래스 정의
class Account:
    # 멤버변수 : 생성자(__init__함수)에서 선언
    def __init__(self, bank, id, name, money):
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money



    # 멤버함수
    def deposit(self, _money):
        self.money += _money

    def withdrow(self, _money):
        self.money -= _money

    def show(self):
        print('-------------------')
        print('은행명 : ', self.bank)
        print('계좌번호 : ', self.id)
        print('입금주 : ', self.name)
        print('현재잔액 : ', self.money)
        print('-------------------')
