import cv2
import numpy as np

def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    # 1. Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Invert
    inverted = 255 - gray

    # 3. Blur
    blur = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)

    # 4. Dodge blend (buat efek sketch halus)
    sketch = dodgeV2(gray, blur)

    # Tampilkan hasil
    cv2.imshow("Pencil Sketch (Real-Time)", sketch)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()