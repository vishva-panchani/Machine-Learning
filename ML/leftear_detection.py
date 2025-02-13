import cv2

img=cv2.imread("girl2.jpeg",cv2.IMREAD_COLOR)
print(img)

face_cascade=cv2.CascadeClassifier("haarcascade_mcs_leftear.xml")
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(grey_img,1.1,4)
print(faces)

for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    
cv2.imshow("Face Detector",img)
cv2.waitKey(10000)
cv2.destroyAllWindows()