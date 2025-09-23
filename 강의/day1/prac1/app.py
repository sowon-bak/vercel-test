from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello-json")
def hello_json():
    return jsonify(message='hello, oz be14')

@app.route("/user/<name>")
def greet(name):
    return jsonify(message=f'{name}님, 오즈 14기 캠프에 오신 것을 환영합니다')