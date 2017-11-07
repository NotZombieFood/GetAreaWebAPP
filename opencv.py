import numpy
import cv2

# read and downscale image
img = cv2.pyrDown(cv2.imread('black.jpg', cv2.IMREAD_UNCHANGED))
# threshold image
# this step is neccessary when you work with contours
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 150, 255, cv2.THRESH_BINARY)
# find contours in image
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
totalPixel = threshed_img.size
whitePixel = cv2.countNonZero(threshed_img)
restar = whitePixel / totalPixel * 100
print(restar)
print(100 - restar)

for cnt in contours:
    # calculate epsilon base on contour's perimeter
    # contour's perimeter is returned by cv2.arcLength
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    # get approx polygons
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # draw approx polygons
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 1)

    # hull is convex shape as a polygon
    hull = cv2.convexHull(cnt)
    cv2.drawContours(img, [hull], -1, (0, 0, 255))

cv2.imshow('contours', threshed_img)
ESC = 27

while True:
    keycode = cv2.waitKey()
    if keycode != -1:
        keycode = 0xFF
        if keycode == ESC:
            break

cv2.destroyAllWindows()