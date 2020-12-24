"""
날짜 : 2020/12/23
이름 : 김남현
내용 : 파이썬 예외처리 실습하기
"""

# try ~ except
if __name__ == '__main__':
    print('main1 실행!')

    num1, num2 = 1, 0
    rs1 = 0
    try:
        rs1 = num1 / num2
    except:
        print('예외발생...')

    print('rs1 : ', rs1)
    print('main1 종료...')

# try ~ except ~ finally
if __name__ == '__main__':
    is_exist = False
    try:
        file = open('C:/Users/82104/Desktop/test.TXT', 'r')
        is_exist = True
    except:
        print('파일이 없습니다.')
    finally:
        # 마지막에 무조건 실행되는 블럭
        if is_exist:
            print('파일을 열었습니다.')
        else:
            print('파일을 추가하세요.')

    print('main2 종료!')


# try ~ except ~ else
if __name__ == '__main__':

    try:
        animal = ['사자', '호랑이', '코끼리', '기린', '곰']

        print('동물을 선택하세요.')
        print('1:사자, 2:호랑이, 3:코끼리, 4:기린, 5:곰')
        
        num = int(input('숫자입력 : '))
        print('선택한 동물 : ', animal[num-1])
    except:
        print('존재하지 않습니다.')
    else:
        # try문이 정상실행 되고 난 후 실행되는 영역
        print('정상 종료되었습니다.')











    print('main3 종료!')


