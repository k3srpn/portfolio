import cv2
import numpy as np
import pytesseract

path = '/Users/ksrpn/k3srpn/org_trim.jpg'
img = cv2.imread(path)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
ret, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)
closed = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
cv2.imshow('b', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()