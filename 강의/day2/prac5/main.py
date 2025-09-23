from flask import Flask, request, jsonify

app = Flask(__name__)

todos = {
    1: "flask 공부하기",
    2: "python 공부하기"
}

@app.route("/todos", methods=["get"])
def get_todos():
    return jsonify(todos)

# @app.route("/todos/<int:todo_id>", methods=["get"])
# def get_todo(todo_id):
#     task = todos.get(todo_id)
#     if not task :
#         return jsonify({"error": "할 일이 없습니다"}),404
#     return jsonify({todo_id: task})

# @app.route("/todos", methods=["post"])
# def create_todos():
#     data = request.get_json()
#     new_id = max(todos.keys()) + 1 if todos else 1
#     # if todos:
#     #     new_id = max(todos.keys()) + 1
#     # else :
#     #     new_id = 1
#     todos[new_id] = data["task"]                 
#     return jsonify({new_id: todos[new_id]}), 201

# @app.route("/todos/<int:todo_id>", methods=["PUT"])
# def update_toddos(todo_id):
#     if todo_id not in todos:
#         return jsonify({"error": "할 일이 없습니다"}), 404
#     data = request.get_json()
#     todos[todo_id] = data["task"]
#     return jsonify({todo_id: todos[todo_id]})

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "할 일을 찾을 수 없습니다"}), 404
    deleted = todos.pop(todo_id)
    return jsonify({"deleted": "삭제 완료!"})

if __name__ == "__main__":
    app.run(debug=True)