
from flask import Flask, render_template, request, jsonify
import hashlib
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient()
db = client.dbsparta

# 서버실행
# 로그인페이지
@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup' ,methods=['POST'])
def signup():

    email_receive = request.form['email_give']
    pw_receive = request.form['pw_give']

    pw_receive = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc = {
        'user_email': email_receive,
        'user_pw': pw_receive
    }

    if not (email_receive and pw_receive):
        return jsonify({'result': 'fail', 'msg': '모두 입력해주세요!'})

    else:
        db.users.insert_one(doc)
        return jsonify({'result': 'success', 'msg': '회원가입 되었습니다!'})

# 로그인페이지를 보여주는 API
@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/index')
def index_page():
    return render_template('index.html')

if __name__ == '__main__':

    app.run('0.0.0.0', port=5000, debug=True)