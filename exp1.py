import cv2

img1 = cv2.imread('Lenna.png')
cv2.imshow('exp1_1', img1)
img2 = cv2.imread('Starry.png')
cv2.imshow('exp1_2', img2)

img_blend = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('exp1_3', img_blend)

cv2.waitKey(0)
