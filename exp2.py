import cv2

# Capture the video using USB cam
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.waitKey(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
