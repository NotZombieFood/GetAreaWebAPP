import numpy
import cv2

# read and downscale image
img = cv2.pyrDown(cv2.imread('colors.jpg', cv2.IMREAD_UNCHANGED))
# threshold image
# this step is neccessary when you work with contours
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 245, 255, cv2.THRESH_BINARY)
# find contours in image
totalPixel = img.size
whitePixel = cv2.countNonZero(threshed_img)
restar = whitePixel / totalPixel * 100
print(restar)
print(100 - restar)
