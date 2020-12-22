"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 반복문 while 실습하기
"""

# while
num1, num5 = 1, 5
while num1 <= num5:
    print('num1 : ', num1)
    num1 += 1

# 1부터 10까지 합
sum1 = 0
start = 1

while start <= 10:
    sum1 += start
    start += 1

print('1부터 10까지 합 : ', sum1)

# 리스트 점수 합
sum2 = 0
score = [60, 72, 82, 86, 94]
i = 0
while i < len(score):
    sum2 += score[i]
    i += 1

print('score 합 : ', sum2)

# break
number = 1

while True:
    if number % 5 == 0 and number % 7 == 0:
        break
    number += 1

print('5와 7의 최소공배수 : ', number)

# continue
total = 0
begin = 1

while begin <= 10:
    begin += 1

    if begin % 2 != 0:
        continue

    total += begin

print('1부터 10까지 짝수합 : ', total)