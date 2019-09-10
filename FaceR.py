import cv2
cascPath ="haarcascade-frontalface-default.xml"
faceCascade=cv2.CascadeClassifier(cascPath)

cap=cv2.VideoCapture(0)
if(cap.isOpened()==False):
    print("Unable to read Camera Output")

while(True):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if(ret==True):
        faces=faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(1,1), flags=cv2.CASCADE_SCALE_IMAGE)
        
        for(x,y,w,h) in faces: cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        
        cv2.imshow('My frame',frame)
        
        if(cv2.waitkey(1) & 0xFF==ord('q')):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindow()
        

