from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger = Swagger(app) # swagger 세팅

@app.route('/hello')
def hello():
    """
    Hello API
    ---
    responses:
      200:
        description: 성공 응답
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello, OZ BE14!"
    """
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)