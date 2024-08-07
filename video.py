# library import
# object of videocapture class
# use it inside a while

import os
import cv2
import sys

path = "LatexAnimation.mp4"

if not os.path.exists(path):
    print(f"File not found: {path}")
    sys.exit(1)
    
cam = cv2.VideoCapture(path)
c = 0
while True:
    state, frame = cam.read()
    if not state:
        break
    # resize
    
    frame1 = cv2.resize(frame,(640,480))
    frame2 = cv2.resize(frame, (0,0), fx=.5,fy=.5)
    cv2.imshow("Video resized", frame1)
    cv2.imshow("Video resized by scale", frame2)
    if cv2.waitKey(10) == ord("q"):
        break
    c+=1
    #print(frame)
print(c)