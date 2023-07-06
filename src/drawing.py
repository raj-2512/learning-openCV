import numpy as np
import cv2

cap = cv2.VideoCapture(2)


while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
    # img = cv2.line(img, (0,height), (width,0), (0,255,0), 5)
    # img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    img = cv2.circle(frame, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Buggy the Clown Raj', (10, height - 10), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()