from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "홈이에요"

@app.route("/hello")
def hello():
    return "안녕하세요"

@app.route("/user/<name>") #동적 라우팅 <>사용
def greet(name):
    return f"{name}님 환영합니다"

if __name__ == "__main__":
    app.run(debug=True)