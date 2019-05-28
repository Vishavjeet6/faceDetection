import cv2
import time
import pandas
from datetime import datetime


first_frame = None
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # difference
    delta_frame = cv2.absdiff(first_frame, gray)

    # threshold  if diff>30 pixels to white else black
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(delta_frame, None, iterations=0)

    # contour area
    (_, cnts, _) = cv2.findCountours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # remove noise and shadows keep the area greater than 1000 pixels
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # show
    cv2.imshow('frame', frame)
    cv2.imshow('Capturing', gray)
    cv2.imshow('delta', delta_frame)
    cv2.imshow('thresh', thresh_delta)

    key = cv2.waitKey(1)
    if key == ord('q'):
            break

video.release()
cv2.destroyAllWindows()