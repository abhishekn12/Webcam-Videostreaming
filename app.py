from flask import Flask,render_template,Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(func(),mimetype= 'multipart/x-mixed-replace;boundary=frame')