import cv2
import time

# to select camera
# 0 for built in camera
video = cv2.VideoCapture(0)

'''
# check return true if python is able to read
# frame represents first image
check, frame = video.read()

# print(check)
# print(frame)

# to stop script
time.sleep(3)

cv2.imshow("Capture", frame)

cv2.waitKey(0)

cv2.destroyAllWindows()

video.release()
'''

a = 1

while True:
    a += 1
    check, frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()