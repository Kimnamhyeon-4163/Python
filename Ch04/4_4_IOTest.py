"""
날짜 : 2020/12/22
이름 : 김남현
내용 : 파이썬 입력함수 실습하기
"""

# 파일 읽기

file =open('C:/Users/82104/Desktop/test.TXT', 'r')
line = file.readline()

print('line : ', line)
file.close()
# 여러줄 파일 읽기
file2 = open('C:/users/82104/desktop/test.TXT','r')

while True:
    line = file2.read()

    if not line:
        break

    print('line : ', line)
file2.close()
# 파일 쓰기

file3 = open('C:/Users/82104/Desktop/test3.TXT', 'w')
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('부탁드려요.\n')
file3.close()
# 구구단 파일 출력
file4 = open('C:/Users/82104/Desktop/test4.TXT', 'w')

for a in range(2, 10):
    file4.write('%d단\n' % a)
    for b in range(1, 10):
        file4.write('%d x %d = %d\n' % (a, b, a*b))
file4.close()

# with문(파일생성과 close를 한번에 실행하는 구문)
with open('C:/Users/82104/Desktop/test5.TXT', 'w') as file5:
    for i in range(11):
        file5.write('★'*i+'\n')

