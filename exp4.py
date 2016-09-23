
import cv2
import numpy as np

# Capture the video using USB cam
cap = cv2.VideoCapture(0)

# Load Face Detector 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    	# Capture frame-by-frame
    	ret, frame = cap.read()
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Detect faces in the frame
	faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30))

	# Draw face rectangles
 	for (x,y,w,h) in faces:
     		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
     
    	# Display the resulting frame
    	cv2.imshow('frame',frame)
    	cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
