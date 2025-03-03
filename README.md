## 📌 프로젝트 소개
이 프로젝트는 **YOLOv8 모델을 사용하여 객체 탐지**를 수행하는 웹 애플리케이션입니다.  
Flask를 기반으로 동작하며, AI가 실시간으로 객체를 탐지하고 결과를 표시합니다.

## 🎯 주요 기능
- 로그인/로그아웃, 좌석 선택/퇴실
- 퇴실 시 YOLOv8 모델을 활용한 실시간 객체 탐지
- 웹을 통해 탐지된 객체 이미지 및 결과 표시

## 🛠️ 기술 스택
- **AI Model:** YOLOv8 (Ultralytics)
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL

👉 **관련 블로그 글**
- 📖 [YOLOv8 학습 및 모델 적용 과정](https://djjin02.tistory.com/205)
- 📖 [객체 탐지 웹 애플리케이션 구현](https://djjin02.tistory.com/207)

---

## 📷 데모 이미지
> YOLOv8을 활용한 객체 탐지 결과 예시  

### 📌 **객체 탐지 화면**
![객체 탐지 결과](https://github.com/JooRi-Kim/yolov8-object-detection/issues/1#issue-2890455443)

### 📌 **웹 애플리케이션 UI**
![웹 UI](https://your-image-url.com/web-ui-example.png)

---

## 📂 프로젝트 구조
- flask_server/
- │── static/             # 정적 파일 (CSS, JS, 이미지)
- │── templates/          # HTML 파일들
- │── yolov5/             # YOLOv8 모델 관련 파일
- │── venv/               # 가상 환경 (Git에 포함되지 않음)
- │── app.py              # Flask 웹 서버
- │── best.pt             # 학습된 YOLOv8 모델 가중치
- │── requirements.txt    # 필요한 패키지 목록
- │── README.md           # 프로젝트 설명

---

## 📖 실행 방법
### 1️⃣ **가상 환경 설정 (선택)**
```bash
python -m venv venv
venv\Scripts\activate  # Windows


