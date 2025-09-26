# 📘 Flask 미니 프로젝트 – 책/영화 리뷰 노트

<br/>

## 🎯 목표
- Flask로 CRUD 기능 전체 구현
- SQLite + SQLAlchemy DB 연동 복습
- 템플릿(Jinja2)으로 UI 구성
- ⭐ 평균 별점 계산 기능 추가

<br/>

## 📝 기능 요구사항
1. 리뷰 작성 (Create)
   - 제목(책/영화 이름), 리뷰 내용, 별점(1~5) 입력
2. 리뷰 목록 보기 (Read)
   - 전체 리뷰 리스트 출력
   - ⭐ 평균 별점 표시
3. 리뷰 수정 (Update)
   - 기존 리뷰 내용/별점 수정
4. 리뷰 삭제 (Delete)
   - 리뷰 삭제 버튼

<br/>

## 🏗️ 프로젝트 구조
```plaintext
project/                    # 프로젝트 루트
 ├── run.py                 # Flask 실행 스크립트 (엔트리포인트)
 ├── requirements.txt       # 의존성 패키지 목록
 ├── instance/              # 로컬 실행 시 생성되는 SQLite DB
 │    └── reviews.db
 └── app/                   # Flask 애플리케이션 코드
      ├── __init__.py       # Flask 앱 생성 + DB 연결 + 블루프린트 등록
      ├── config.py         # 환경 설정 (DB URL, DEBUG 옵션 등)
      ├── models.py         # DB 모델 정의 (Review 모델)
      ├── services/         # 서비스 계층 (비즈니스 로직)
      │    └── review_service.py
      ├── routes/           # 라우트 계층 (URL 처리 + 템플릿 렌더링)
      │    └── review_routes.py
      ├── templates/        # HTML 템플릿 (Jinja2 + Tailwind)
      │    ├── index.html   # 리뷰 목록 + 평균 별점
      │    ├── new.html     # 리뷰 작성 폼
      │    └── edit.html    # 리뷰 수정 폼
      └── static/           # 정적 파일 (CSS, JS, 이미지): 지금은 비어 있음
```
