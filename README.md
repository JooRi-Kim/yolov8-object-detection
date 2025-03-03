## 📌 프로젝트 소개
- YOLOv8 모델을 활용한 객체 탐지 Flask 웹 애플리케이션입니다.
- AI가 실시간으로 핸드폰, 노트북, 태블릿, 지갑, 가방, 펜을 탐지하여 결과를 표시합니다.
- 실내 공간(스터디카페)에서 주로 사용되는 물건들로 객체를 선정하였습니다.


---


## 📅 개발 기간
- 24/10/01 ~ 24/11/14


---


## 👨‍💻 개발 담당
- Backend (김주리)
  - Flask 서버 개발(app.py)
  - 객체 탐지 DB 설계 및 구현
  - 웹과 YOLOv8 모델 연동
- AI (김은수)
  - AI 데이터 수집 및 정제
  - YOLOv8 모델 학습
  - 모델 최적화
- Frontend, 기능 개발 (양한별)
  - UI 구현
  - 로그인/회원가입 기능 구현
- H/W, 기능 개발 (이승헌)
  - 좌석 선택/퇴실 기능 구현
  - 젯슨나노 연동
- H/W (조윤서)
  - 젯슨나노 연동


---


## 🛠️ 기술 스택
- **AI Model**: YOLOv8 (Ultralytics)
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL


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
![핸드폰 탐지](https://private-user-images.githubusercontent.com/122363990/418486603-81e1d3bd-daea-4929-a646-038f1f9a94a6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTAzNTYsIm5iZiI6MTc0MDk5MDA1NiwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg2NjAzLTgxZTFkM2JkLWRhZWEtNDkyOS1hNjQ2LTAzOGYxZjlhOTRhNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODIwNTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZTA1Yjc1MmQxMmNkNTE0ZTNkOWU5ZmFkYWFmZTVmMGQ1NjllMTAyMmQ4ZGQ2ZGQzODRiOTVlYTU4NDAwN2U2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.nrrC2gjFvrTz8H8T58YuFyAyBWpPvkjBOU_9qf7aNBM)


### ✅ 핸드폰(phone) 객체 탐지 로그
![핸드폰 탐지](https://private-user-images.githubusercontent.com/122363990/418486005-2e9cc696-f124-4b00-870b-f97a6081ab75.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTAyNjksIm5iZiI6MTc0MDk4OTk2OSwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg2MDA1LTJlOWNjNjk2LWYxMjQtNGIwMC04NzBiLWY5N2E2MDgxYWI3NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODE5MjlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03OTVlYjljYjJhNzUzNzQ3MmM5OWE5ZDE4MWQ1ZDhhMjI2NGUwN2I0OTM2NjE5YjY3ZGExNTliNTVjN2ZmM2E2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.6fLeBec7DgZob9pLlk5KRYeu2PQxrlExUjs8qrHAmQE)


### ✅ 10초동안 객체를 탐지하고, 가장 높은 신뢰도를 가지는 하나의 결과만 DB에 저장 
![핸드폰 탐지 결과 화면](https://private-user-images.githubusercontent.com/122363990/418486124-82204edf-3ad4-4335-bc40-912d17278b0e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTAyODIsIm5iZiI6MTc0MDk4OTk4MiwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg2MTI0LTgyMjA0ZWRmLTNhZDQtNDMzNS1iYzQwLTkxMmQxNzI3OGIwZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODE5NDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kNGRiODdmMmFmMjc2M2Y2Y2Y2ZWY2ZjdlMGMwM2JkMWNiOTg2NmNjNmU4MmQ2NjIzNGU3N2FmOTllMDMwZDFlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.jtxLzZVH97O9uezOHCaIlC5v1tb8ZmxDpjpc72_fOTM)


### ✅ 펜(pen) 탐지 결과 화면
![펜 탐지](https://private-user-images.githubusercontent.com/122363990/418487983-c9faca76-26ac-4584-a1a3-6da41fcc6de6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTA3NjgsIm5iZiI6MTc0MDk5MDQ2OCwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg3OTgzLWM5ZmFjYTc2LTI2YWMtNDU4NC1hMWEzLTZkYTQxZmNjNmRlNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODI3NDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04YTViMjljNWYwMmE3OWJkM2Y3NjMzMDUyZmY5ODljZDMwOTc2MDU5NzdiMzE4NTA5OGQzOTU0MDE3NmJiMzBmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.LSozBeiUl4XcclEPJ9-wLSU4Q7r37zspOqLbyFa9_LU)


### ✅ 펜(pen) 객체 탐지 로그
![펜 탐지](https://private-user-images.githubusercontent.com/122363990/418488194-35637745-5185-49e4-a822-8003ea9fd1d4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTA3NjgsIm5iZiI6MTc0MDk5MDQ2OCwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg4MTk0LTM1NjM3NzQ1LTUxODUtNDllNC1hODIyLTgwMDNlYTlmZDFkNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODI3NDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zZTJiODM5NGU3MDM4OThhMThlOWUyMjVmOWQ5YWMyYWQ2ZmZiMjMzMjRjNmU1NzIxNjNmNzU1NzgwZWVhZTkzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.3V-GFh4sG8ByQb89t7kJPRBGKV06m9J7n55DTe0EaUU)


### ✅ 핸드폰(phone)과 노트북(labtop) 탐지 결과 화면
![핸드폰과 노트북 탐지](https://private-user-images.githubusercontent.com/122363990/418488327-8530cd2d-ce4b-4eb7-8f97-c9552694a738.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTA3OTgsIm5iZiI6MTc0MDk5MDQ5OCwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg4MzI3LTg1MzBjZDJkLWNlNGItNGViNy04Zjk3LWM5NTUyNjk0YTczOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODI4MThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MWU0ZDRlZmVhMGNjM2QwMzQ2OWM3OTY3MzZhZDdhOTQ4YTFhYWRlMWIxZGJjMjRjYTcxYzc5OThiNzZhNTQ0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.HE3COEvTKsvtQp0hqxyAzNdJ3bmd-Qyay-xrYMLxeTk)


### ✅ 핸드폰(phone)과 노트북(labtop) 객체 탐지 로그
![핸드폰과 노트북 탐지](https://private-user-images.githubusercontent.com/122363990/418488391-cbddbe18-3de9-42b5-81ea-0f125fb9712c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDA5OTA3OTksIm5iZiI6MTc0MDk5MDQ5OSwicGF0aCI6Ii8xMjIzNjM5OTAvNDE4NDg4MzkxLWNiZGRiZTE4LTNkZTktNDJiNS04MWVhLTBmMTI1ZmI5NzEyYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwM1QwODI4MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OWM2OTMyYTk2ZWE0ZjZmNzhiZThkYzJhNTM4MjM0YWE2MDU1NTJkYzZmNjE2ZWY3NGQ3YmM4Mzk4MjQzNWU2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.4Uv2ovdaLMwPqmhZNUt24BL8wjsM6h4Lwq9I_piIDmY)


---


## 🔗 블로그: 프로젝트 관련 포스트
- [YOLOv8 학습 및 모델 적용 과정](https://djjin02.tistory.com/205)
- [객체 탐지 웹 애플리케이션 구현](https://djjin02.tistory.com/207)


---

