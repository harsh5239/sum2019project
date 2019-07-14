import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier(r"C:\Users\HARSH SONI\Desktop\background\haarcascade_frontalface_default.xml")

video_capture  =cv2.VideoCapture(0)
while(True):
    idx=0

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        idx += 1
        print (idx)
        cv2.putText(frame,str(idx),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,.7,(150,150,0),2)
    cv2.putText(frame,"total-faces::"+str(idx),(10,480),cv2.FONT_HERSHEY_SIMPLEX , 2,(0,255,255),2,cv2.LINE_AA)


    cv2.imshow('img',frame)
    if(cv2.waitKey(1)==ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()
