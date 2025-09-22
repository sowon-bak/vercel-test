from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet")
def greet():
    name = request.args.get("name","OZ") #(입력받는값,기본값)
    return render_template("greet.html",name=name)

###### 동적라우팅
# @app.route("/greet/<name>")
# def greet(name):
#     return render_template("greet.html", name=name)

if __name__=="__main__":
    app.run(debug=True)