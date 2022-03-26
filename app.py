from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route("/upload", methods=['POST'])
def upload():
    img = request.files['image']
    print(img)
    return jsonify({'msg':'저장에 성공했습니다.'})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)