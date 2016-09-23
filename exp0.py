import cv2

img = cv2.imread('Lenna.png')
cv2.imshow('exp0', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('exp0_2', img_gray)
cv2.waitKey(0)

# 
print img

cv2.destroyAllWindows()

