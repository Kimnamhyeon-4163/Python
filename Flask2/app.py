"""
날짜 : 2020/12/24
이름 : 김남현
내용 : 파이썬 Flask 조건문, 반복문
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    tit = '파이썬 Flask 조건문, 반복문 실습하기'
    num = 12
    cities = ['서울', '대전', '대구', '부산', '광주']


    return render_template('/index.html', tit=tit, num=num, cities=cities)


if __name__=='__main__':
    app.run()