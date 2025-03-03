import time
from flask import Flask, request, jsonify, render_template, send_file, session, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from ultralytics import YOLO
from PIL import Image, ImageDraw
import io
import os
import gdown
import numpy as np
import cv2
from io import BytesIO
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask 앱 설정
app = Flask(__name__, template_folder='templates')  # 'templates' 폴더 경로
app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))

# MySQL 설정
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'study_cafe_db')
mysql = MySQL(app)

# 모델 다운로드 및 로드
model_path = 'best.pt'
file_id = '1L0dkL2h-WPRXv9OKpsCiVEKKyUcvlCDZ'
if not os.path.exists(model_path):
    logger.info("Google Drive에서 모델을 다운로드 중...")
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, model_path, quiet=False)
    logger.info(f"{model_path} 다운로드 완료!")

model = YOLO(model_path)
logger.info("YOLO 모델이 성공적으로 로드되었습니다.")

def save_detection_to_db(class_name, confidence, bbox):
    try:
        cursor = mysql.connection.cursor()
        query = """
        INSERT INTO detections (class_name, confidence, bbox)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (class_name, confidence, f"{bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}"))
        mysql.connection.commit()
        cursor.close()
        logger.info(f"{class_name} 클래스가 신뢰도 {confidence}로 데이터베이스에 저장되었습니다.")
    except Exception as e:
        logger.error(f"데이터베이스에 데이터를 저장하는 데 실패했습니다: {e}")

@app.route('/exit', methods=['POST'])
def exit_seat():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT seat_number FROM seats WHERE occupied_by = %s", [session['user_id']])
    seat = cursor.fetchone()

    if seat:
        cursor.execute("UPDATE seats SET is_occupied = FALSE, occupied_by = NULL WHERE seat_number = %s", [seat[0]])
        mysql.connection.commit()
        cursor.close()

        return render_template('exit_countdown.html', seat_number=seat[0])

    cursor.close()
    return "You are not occupying any seat.", 400

@app.route('/start-detection', methods=['POST'])
def start_detection():
    seat_number = request.form.get('seat_number')
    cursor = mysql.connection.cursor()

    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        cursor.close()
        logger.error("웹캠을 열 수 없습니다.")
        print("외부 카메라가 열리지 않습니다.")
        return "웹캠을 열 수 없습니다.", 500

    start_time = time.time()
    detected_items = []  # 탐지된 항목을 저장할 리스트
    captured_image_path = None  # 캡처된 이미지 경로

    while time.time() - start_time < 2:
        ret, frame = cap.read()
        if not ret:
            break

        # 첫 번째 프레임을 캡처하여 저장
        if not captured_image_path:
            captured_image_path = 'static/captured_image.jpg'
            cv2.imwrite(captured_image_path, frame)

        _, img_encoded = cv2.imencode('.jpg', frame)
        img_bytes = img_encoded.tobytes()

        try:
            img = Image.open(BytesIO(img_bytes)).convert('RGB')
            results = model(img)
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()
                    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
                    confidence = float(box.conf[0])
                    class_id = int(box.cls[0])
                    class_name = model.names[class_id]

                    # 탐지된 항목 추가
                    detected_items.append(class_name)

        except Exception as e:
            logger.error(f"추론 중 오류가 발생했습니다: {e}")
            continue

    cap.release()

    # 중복 제거 및 고유 탐지 항목 리스트화
    unique_detected_items = list(set(detected_items))

    if unique_detected_items:
        try:
            for item in unique_detected_items:
                cursor.execute(
                    "INSERT INTO lost_items (user_id, seat_number, item_description) VALUES (%s, %s, %s)",
                    (session['user_id'], seat_number, item)
                )
            mysql.connection.commit()
        except Exception as e:
            mysql.connection.rollback()
            cursor.close()
            logger.error(f"데이터베이스에 분실물을 저장하는 중 오류가 발생했습니다: {e}")
            return f"데이터베이스에 분실물을 저장하는 중 오류가 발생했습니다: {e}", 500

        cursor.close()
        return render_template('detection_result.html', lost_item=unique_detected_items, captured_image=captured_image_path)
    else:
        cursor.close()
        return render_template('detection_result.html', lost_item=None, captured_image=captured_image_path)


@app.route('/')
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM seats WHERE occupied_by = %s", [session['user_id']])
    seat = cursor.fetchone()
    cursor.close()

    if seat:
        return render_template('home.html', is_occupied=True)
    else:
        return render_template('home.html', is_occupied=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            logger.warning(f"회원가입 시도: 중복 사용자 이름 '{username}'")
            return "Username already exists. Please choose a different username.", 400

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
            mysql.connection.commit()
            logger.info(f"새 사용자 등록: {username}")
        except Exception as e:
            mysql.connection.rollback()
            cursor.close()
            logger.error(f"회원가입 중 오류 발생: {e}")
            return f"An error occurred during registration: {e}", 500

        cursor.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = username

            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM seats WHERE occupied_by = %s", [session['user_id']])
            seat = cursor.fetchone()
            cursor.close()

            session['is_occupied'] = True if seat else False
            return redirect(url_for('home'))

        else:
            return "Invalid credentials", 401

    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        logger.info(f"{session['username']} 사용자가 로그아웃했습니다.")
    session.clear()
    return redirect(url_for('login'))

@app.route('/select-seat', methods=['GET', 'POST'])
def select_seat():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        seat_number = request.form['seat_number']
        cursor.execute("SELECT * FROM seats WHERE seat_number = %s AND is_occupied = FALSE", [seat_number])
        seat = cursor.fetchone()
        if seat:
            cursor.execute("UPDATE seats SET is_occupied = TRUE, occupied_by = %s WHERE seat_number = %s",
                           (session['user_id'], seat_number))
            mysql.connection.commit()
            cursor.close()
            logger.info(f"사용자 {session['username']}가 좌석 {seat_number}을 예약했습니다.")
            return redirect(url_for('home'))
        else:
            cursor.close()
            logger.warning(f"좌석 예약 시도: 좌석 {seat_number}은 이미 예약됨.")
            return "Seat is not available or already occupied.", 400

    cursor.execute("SELECT * FROM seats")
    seats = cursor.fetchall()
    cursor.close()
    return render_template('select_seat.html', seats=seats)

@app.route('/lost-items')
def lost_items():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT seat_number, item_description, timestamp FROM lost_items WHERE user_id = %s",
                       [session['user_id']])
        items = cursor.fetchall()
        logger.info(f"사용자 {session['username']}의 분실물 목록을 불러왔습니다.")
    except Exception as e:
        cursor.close()
        logger.error(f"분실물 목록 불러오기 오류: {e}")
        return f"데이터베이스에서 분실물을 불러오는 중 오류가 발생했습니다: {e}", 500
    cursor.close()
    return render_template('lost_items.html', items=items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
