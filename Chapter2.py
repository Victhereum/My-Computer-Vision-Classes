import cv2
import numpy as np

img = cv2.imread('Resources/Abe.jpg')
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 250)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErod =cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('GrayImage', imgGray)
cv2.imshow('BlurImage', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Image', imgDilation)
cv2.imshow('Eroded Image', imgErod)

cv2.waitKey(0)