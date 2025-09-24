from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# db 설정
BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(INSTANCE_DIR, "todos.db")}"
engine = create_engine(
    DATABASE_URL,
    echo=True
)

Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)

    def __repr__(self): # 변경 결과 깨끗하게 보기
        return f"<Todo(id={self.id}, task='{self.task}')"

Base.metadata.create_all(bind=engine)

# api

@app.route("/todos", methods=["get"])
def get_todos():
    db = Sessionlocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{'id': t.id, 'task': t.task} for t in todos])

@app.route("/todos/<int:todo_id>", methods=["get"])
def get_todo(todo_id):
    db = Sessionlocal()
    todo = db.query(Todo).get(todo_id)
    db.close()
    if not todo :
        return jsonify({"error": "할 일이 없습니다"}), 404    
    return jsonify({'id': todo.id, 'task': todo.task})

@app.route("/todos", methods=["post"])
def create_todos():
    data = request.get_json()
    db = Sessionlocal()
    new_todo = Todo(task=data['oz'])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo) # commit 이후로 자동 생성된 id를 불러오기 위해
    db.close()            
    return jsonify({'id': new_todo.id, 'task': new_todo.task}), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_toddos(todo_id):
    data = request.get_json()
    db = Sessionlocal()
    # db에서 수정할 항목 찾기
    todo = db.query(Todo).get(todo_id)
    if not todo : # 못찾으면 db닫고 404 반환
        db.close()
        return jsonify({"error": "할 일이 없습니다"}), 404
    
    # 있으면 업데이트
    todo.task = data["task"]
    db.commit

    # 이미 있던 거라 id 값 불러오기 위해 refresh할 필요는 없고 그냥 업데이트 된 정보
    updated = {'id': todo.id, 'task': todo.task}
    db.close()
    return jsonify(updated)

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    db = Sessionlocal()

    # db에서 항목 찾기
    todo = db.query(Todo).get(todo_id)
    if not todo: # 몾찾으면 db닫고 404 반환
        db.close()
        return jsonify({"error": "할 일을 찾을 수 없습니다"}), 404
    
    # 데이터 삭제
    db.delete(todo)
    db.commit()
    db.close()
    return jsonify({"deleted": "삭제 완료!"})

if __name__ == "__main__":
    app.run(debug=True)