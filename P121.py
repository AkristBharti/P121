import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
image = cv2.imread("undertale.jpg")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
    
    ublack = np.array([104,153,70])
    lblack = np.array([30,30,0])
    mask = cv2.inRange(frame, lblack, ublack)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame-res
    f = np.where(f == 0, image, f)
    cv2.imshow("cap", frame)
    cv2.imshow("mask", f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
