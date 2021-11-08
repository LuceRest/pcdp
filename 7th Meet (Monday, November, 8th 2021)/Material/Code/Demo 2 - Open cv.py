# ----------| Transaltion |----------


import cv2
import numpy as np

img = cv2.imread('messi5.jpg', 0)
cv2.imshow('messi_ori', img)
rows, cols = img.shape

M = np.float32([[1, 0, 200], [0, 1, 150]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
