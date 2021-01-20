import cv2 as cv
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailble = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailble:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                               None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageblank = np.zeros((height, width, 3), np.uint8)
        hor = [imageblank] * rows
        hor_con = [imageblank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

img = cv.imread('Resources/Abe.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))
# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img, img))
#
# cv.imshow('Horizontal', imgHor)
# cv.imshow('Horizontal', imgVer)
cv.imshow('ImageStack', imgStack)

cv.waitKey(0)