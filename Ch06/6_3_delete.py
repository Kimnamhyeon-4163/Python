"""
날짜 : 2020/12/24
이름 : 김남현
내용 : 파이썬 데이터베이스 프로그래밍
"""
import pymysql as db

# 1단계 - 데이터베이스 접속
conn = db.connect(host='192.168.10.114',
                  user='knh',
                  password='1234',
                  db='knh',
                  charset='utf-8')


# 2단계 - 쿼리문 실행객체 생성
cursor = conn.cursor()
# 3단계 - 쿼리문 실행
sql = "DELETE FROM `USER1` WHERE `uid`='P101';"
cursor.execute(sql)
# 4단계 - 쿼리문 실행 확정
conn.commit()
# 5단계 - 데이터베이스 종료
conn.close()

print('DELETE 완료...')