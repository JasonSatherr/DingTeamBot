import io
import time
import picamera
import cv2
import numpy as np

# Create the in-memory stream

stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')

data = np.frombuffer(stream.getvalue(), dtype=np.uint8)

image = cv2.imdecode(data, 1)


face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
# image = cv2.imread("./forever_photos/sather.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 8)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("./photos/sather.jpeg", image)