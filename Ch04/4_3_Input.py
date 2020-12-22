"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 입력함수 실습하기
"""

#입력함수
num = input('숫자입력 : ')

#출력함수
print('num : ', num)

while True:
    score = input('점수 입력(종료는-1) : ')

    score = int(score)

    if score == -1:
        break

    grade(score)

print('프로그램종료...')
