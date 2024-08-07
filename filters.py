import cv2
import numpy as np

path = r"D:\the Witcher\The_Witcher_S01_E01_WebRip_Dual_Audio_Hindi_5_1_+_English_5_1_720p.mkv"
video = cv2.VideoCapture(path)
while True:
    state, frame = video.read()
    if not state:
        break
    
    frame = cv2.resize(frame,(0,0),fx=.6,fy=.6)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    gray_or = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
    
    s1 = cv2.hconcat([frame, cv2.merge([gray,gray,gray])])
    s2 = cv2.hconcat([rgb,gray_or])
    all = cv2.vconcat([s1,s2])
    
    h,w,_ = all.shape
    
    all =cv2.putText(all,"Orignal",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),4)
    all =cv2.putText(all,"Grayscale",(50+w//2,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),4)
    all =cv2.putText(all,"RGB",(50,100+h//2),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),4)
    all =cv2.putText(all,"HSV",(50+w//2,100+h//2),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),4)
    
    
    cv2.imshow("video",all)
    
   
    # cv2.imshow("video bw",gray)
    # cv2.imshow("video rgb",rgb)
    # cv2.imshow("video hsv",hsv)
    print(gray.shape)
    if cv2.waitKey(1) == ord("q"):
        break