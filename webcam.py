import cv2

cam = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)

c=0
while cam.isOpened() and cam1.isOpened():
    state, frame = cam.read()
    state1, frame1 = cam1.read()
    if not state and not state1:
        break
    cv2.imshow("Webcam", frame)
    cv2.imshow("Webcam1", frame1)
    c+=1
    if cv2.waitKey(10) == ord("q"):
        break
    
print(c)