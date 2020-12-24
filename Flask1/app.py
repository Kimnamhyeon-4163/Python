"""
날짜 : 2020/12/24
이름 : 김남현
내용 : 파이썬 웹 프로그래밍(Flask)
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!!!</h1>'

@app.route('/hello')
def hello():
    return render_template('/hello.html')



if __name__ == '__main__':
    app.run()
