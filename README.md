## 📌 프로젝트 소개
- YOLOv8 모델을 활용한 객체 탐지 Flask 웹 애플리케이션입니다.
- AI가 실시간으로 핸드폰, 노트북, 태블릿, 지갑, 가방, 펜을 탐지하여 결과를 표시합니다.
- 실내 공간(스터디카페)에서 주로 사용되는 물건들로 객체를 선정하였습니다.


---


## 📅 개발 기간
- 24/10/01 ~ 24/11/14


---


## 👨‍💻 개발 담당
- Backend
  - Flask 서버(app.py) 개발
  - DB 구현
  - 웹과 YOLOv8 모델 연동


---


## 🛠️ 사용 기술
- AI: YOLOv8 (Ultralytics)
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Database: MySQL


---


## 🎯 주요 기능
- 회원가입/로그인/로그아웃
- 좌석 선택/퇴실
- 퇴실 시 YOLOv8 모델을 활용한 실시간 분실물(객체) 탐지
- 웹을 통해 분실물 사진 및 결과 표시


---


## 📂 프로젝트 구조
```
📂 flask_server/
├── 📂 static/             # 정적 파일 (CSS, JS, 이미지)
├── 📂 templates/          # HTML 파일
├── 📂 yolov8/             # YOLOv8 모델 관련 파일 (Git에 포함되지 않음)
├── 📂 venv/               # 가상 환경 (Git에 포함되지 않음)
├── 📂 app.py              # Flask 웹 서버
├── 📂 best.pt             # 학습된 YOLOv8 모델 가중치 (Git에 포함되지 않음)
├── 📂 requirements.txt    # 필요한 패키지 목록
└── 📂 README.md           # 프로젝트 설명
```


---


## 📷 결과
### ✅ 핸드폰(phone) 탐지 결과 화면
![image](https://github.com/user-attachments/assets/a10e4540-7c80-4109-9bd8-6df4193f762b)


### ✅ 핸드폰(phone) 객체 탐지 로그
![image](https://github.com/user-attachments/assets/d8564a10-7ed5-410f-af4f-d537089ac659)


### ✅ 10초동안 객체를 탐지하고, 가장 높은 신뢰도를 가지는 하나의 결과만 DB에 저장 
![image](https://github.com/user-attachments/assets/452a4f4a-bd6d-426d-9033-7a55f4fbc231)


### ✅ 펜(pen) 탐지 결과 화면
![image](https://github.com/user-attachments/assets/26137140-7b4e-415b-ba70-4c8904d34cbf)


### ✅ 펜(pen) 객체 탐지 로그
![image](https://github.com/user-attachments/assets/917782fc-dc88-401a-b4d6-66261be416ea)


### ✅ 핸드폰(phone)과 노트북(laptop) 탐지 결과 화면
![image](https://github.com/user-attachments/assets/e54f2610-014a-4746-916d-0e18a3fe8e0f)


### ✅ 핸드폰(phone)과 노트북(laptop) 객체 탐지 로그
![image](https://github.com/user-attachments/assets/d4aa791b-7b8c-4786-9c3f-2222a8982b28)


---


## 🔗 블로그: 프로젝트 관련 포스트
- [YOLOv8 학습 및 모델 적용 과정](https://djjin02.tistory.com/205)
- [객체 탐지 웹 애플리케이션 구현](https://djjin02.tistory.com/207)


---

