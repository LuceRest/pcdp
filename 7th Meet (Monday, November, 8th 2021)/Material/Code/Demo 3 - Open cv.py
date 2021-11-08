# ----------| Rotation |----------


import cv2
import numpy as np

img = cv2.imread('messi5.jpg', -1)
cv2.imshow('messi_ori', img)
rows, cols, rgb = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 50, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('messi_rot', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
