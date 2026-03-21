import numpy as np
import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt
import sys

model = YOLO("wonderweiss_model.pt")

print("Enter File Name")
filename = sys.argv[1]
print("Hello. Meet WonderWeiss") 
print("How Would You Like Him To Detect Today?") 
print("1. Photo") 
print("2. Video") 
print("3. Webcam")

command = input()
match command:
    case 1:
     img = cv2.imread(filename)
     detect = model(img,conf=.98)
     for d in detect:
        d.show()
    case 2:
      capture = cv2.VideoCapture("filename")

      while capture.isOpened():
            ret, frame = capture.read()

            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            detectVideo = model(frame,conf=0.5)

            visual_frame = detectVideo[0].plot()

            cv2.imshow("video", visual_frame)

            if cv2.waitKey(1) == ord('q'):
                break
            capture.release()
            cv2.destroyAllWindows()
    case 3:
      capture = cv2.VideoCapture(0)

      while capture.isOpened():
            ret, frame = capture.read()

            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            detectVideo = model(frame,conf=0.5)

            visual_frame = detectVideo[0].plot()
            cv2.imshow("video", visual_frame)
            cv2.putText(frame,"test", (40,40),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            if cv2.waitKey(1) == ord('q'):
                break

capture.release()
cv2.destroyAllWindows()