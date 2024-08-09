import cv2

cam = cv2.VideoCapture(0)


def no_action(x):
    pass

cv2.namedWindow("result")
cv2.createTrackbar("blocksize","result",2,10,no_action)
cv2.createTrackbar("ksize","result",3,31,no_action)
cv2.createTrackbar("k","result",1,100,no_action)

while cam.isOpened():
    state, frame = cam.read()
    if not state:
        break
    #logic
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bs = cv2.getTrackbarPos("blocksize","result")
    ks = cv2.getTrackbarPos("ksize","result")
    k = cv2.getTrackbarPos("k","result")
    try:
        result = cv2.cornerHarris(gray,bs,ks,k/100)
        result = cv2.dilate(result,None)
        frame[result>0.01*result.max()]=[0,0,225]
    except:
        h,w,_ = frame.shape
        cv2.rectangle(frame,(100,100),(w-100,h-100),(0,0,255),5)
    cv2.imshow("result",frame)
    if cv2.waitKey(1) == ord("q"):
        break