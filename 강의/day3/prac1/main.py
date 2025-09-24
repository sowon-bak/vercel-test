from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# base 클래스 정의
Base = declarative_base()

# 테이블 user 모델 정의
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    def __repr__(self): # 변경 결과 깨끗하게 보기
        return f"<User(id={self.id}, name='{self.name}')"
    

# 데이터베이스 연결 (sqlite 사용)
engine = create_engine("sqlite:///users.db", echo=True)

# 테이블 생성
Base.metadata.create_all(bind=engine)

# session 준비
Sessionlocal = sessionmaker(bind=engine)

def run_single():

    db = Sessionlocal()

    # create
    new_user = User(name="oz")
    db.add(new_user)
    db.commit()
    
    # read
    # users = db.query(User).all() # 모든 유저 조회
    user = db.query(User).first() # 단일 유저 조회
    print(user)

    # update
    user.name = "리버"
    db.commit()

    # 변경 확인 read
    modified_user = db.query(User).first()
    print('유저 수정 조회 완료:', modified_user)  

    # delete
    db.delete(modified_user)
    db.commit()

    db.close()

def run_bulk():

    db = Sessionlocal()

    # create
    new_users = [User(name='oz_한율'),User(name='oz_조교'),User(name='oz_바부')]
    db.add_all(new_users)
    db.commit()

    # read
    users = db.query(User).all()
    for user in users:
        print(user)

    # 조건조회
    oz_user = db.query(User).filter(User.name == 'oz_한율').first()
    # print('한율님 찾기:', oz_user)

    # 패턴 검색
    oz_users = db.query(User).filter(User.name.like('oz_%')).all()
    print('oz 포함된 이름 찾기:', oz_users)

    # update
    for u in oz_users:
        u.name = u.name + "_NEW"
    db.commit()

    # delete
    db.query(User).delete()
    db.commit
    print('삭제완료')

    db.close()

if __name__ == "__main__":
    # run_single()
    run_bulk()
