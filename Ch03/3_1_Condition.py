"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 조건문 실습하기
"""
#if
num1,num2 = 1,2
if num1 >0:
    print('num1은 0보다크다.')

if num1 < num2:
    print('num1은 num2보다 작다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 >1:
    print('num1은 0보다 크고 그리고 num2는 1보다 크다.')

#if ~else
num3,num4 =3,4

if num3 > num4:
    """조건이 참일때"""
    print('num3은 num4보다 크다.')
else:
    """조건이 거짓일때"""
    print('num3은 num4보다 작다.')

#if~elif~else
if num1 > num2:
    print('num1보다 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장크다.')

#연습문제
score = 86
if score >= 90 and score <= 100:
    print('a 입니다.')
elif 80 <= score <90:
    print('b 입니다.')
elif 70 <= score <80:
    print('c 입니다.')
elif 60 <= score <70:
    print('d 입니다.')
else:
    print('f 입니다.')



