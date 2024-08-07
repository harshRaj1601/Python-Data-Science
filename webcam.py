import cv2

cam = cv2.VideoCapture(0)
c=0
while cam.isOpened():
    state, frame = cam.read()
    if not state:
        break
    # resize
    cv2.imshow("Webcam", frame)
    print(frame.shape)
    c+=1
    if cv2.waitKey(10) == ord("q"):
        break
    
print(c)