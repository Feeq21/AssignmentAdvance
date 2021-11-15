import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('D:/KOTOCLASS/secondmonth/cv-master/advance/assets/class_pic.png')

# show image
cv2.imshow('Display Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()