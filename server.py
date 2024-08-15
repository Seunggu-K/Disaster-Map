from flask import Flask, render_template
import pandas as pd
import sqlite3
import os
from flask_cors import CORS # flask 버전을 2.2.2로 해야함 pip install flask==2.2.2

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template('test.html')

@app.route('/api')
def hello_world_api():
    # SQLite 데이터베이스 연결 생성(파일이 없으면 생성)
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__),'airflow','db','main.db'))

    # 연결 속성 설정
    conn.text_factory = str  # 기본값이 str이며, 이는 UTF-8로 인코딩됨을 의미합니다.

    # SQL 쿼리를 사용하여 데이터를 DataFrame으로 로드
    query = "SELECT * FROM location_data"
    df = pd.read_sql_query(query, conn)

    return df.to_json(orient="table")

if __name__ == '__main__':
    app.run(debug=True, port=80)