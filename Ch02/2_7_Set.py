"""
날짜 : 2020/12/21
이름 : 김남현
내용 : 파이썬 자료구조 집합 실습하기
"""

# 집합
set1 = set([1, 2, 3, 4, 5, 3, 4])
set2 = set('Hello World')

print('set1 : ', set1)
print('set2 : ', set2)

# 집합 출력 -> 리스트 or 튜플로 변환 후 출력
list1 = list(set1)
tuple1 = tuple(set2)

print('list1 : ', list1)
print('tuple1 : ', tuple1)