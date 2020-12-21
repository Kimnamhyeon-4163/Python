"""
날짜 : 2020/12/21
이름 : 김남현
내용 : 파이썬 자료구조 딕셔너리 실습하기
"""

# 딕셔너리(파이썬의 JSON)
dic1 = {1: 'C++', 2: 'Java', 3: 'Python'}
dic2 = {
    'kor': '대한민국',
    'usa': '미국',
    'jpn': '일본',
    'chi': '중국'
}

dic3 = {
    101: [1, 2, 3],
    102: ['김유신', '김춘추', '장보고'],
    103: [True, False, True]
}

# 딕셔너리 출력
print('dic1 : ', dic1)
print('dic2 : ', dic2)
print('dic3 : ', dic3)

print('dic1[1] : ', dic1[1])
print("dic2['kor'] : ", dic2['kor'])
print('dic3[102] : ', dic3[102])
print('dic3[102][1] : ', dic3[102][1])

# 딕셔너리 추가
dic1[4] = 'Javascript'
print('dic1 : ', dic1)

dic2['aus'] = '호주'
print('dic2 : ', dic2)

dic3[104] = (7, True, 'Hello')
print('dic3 : ', dic3)

# 딕셔너리 제거
del dic1[1]
print('dic1 : ', dic1)