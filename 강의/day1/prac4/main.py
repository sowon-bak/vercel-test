from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template("hello.html",name='성우')

@app.route("/user/<username>")
def user(username):
    return render_template("hello.html",username=username)

@app.route("/fruits")
def fruits():
    fruits = ['사과','딸기','수박','포도','바나나']
    return render_template("fruits.html",fruits=fruits)

if __name__=="__main__":
    app.run(debug=True)