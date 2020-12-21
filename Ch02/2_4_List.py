"""
날짜 : 2020/12/21
이름 : 김남현
내용 : 파이썬 자료구조 리스트 실습하기
"""
# 리스트
list1 = [1, 2, 3, 4, 5]

print('list1[0] : ', list1[0])
print('list1[2] : ', list1[2])
print('list1[4] : ', list1[4])

list2 = [1, 1.23, True, '홍길동']
print('list2[0] : ', list2[0])
print('list2[1] : ', list2[1])
print('list2[2] : ', list2[2])
print('list2[3] : ', list2[3])

list3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print('list3[0] : ', list3[0])
print('list3[0][1] : ', list3[0][1])
print('list3[2][1] : ', list3[0][1])

# 리스트 더하기
animal1 = ['사자', '호랑이']
animal2 = ['곰', '코끼리', '기린']
animal3 = animal1 + animal2
print('animal3 : ', animal3)

# 리스트 수정, 삭제
count = [1, 2, 3, 4, 5]

count[1] = 7
print('count : ', count)

count[2:3] = [8, 9]
print('count : ', count)

count[1:3] = []
print('count : ', count)

del count[0]
print('count : ', count)

del count[1:4]
print('count : ', count)