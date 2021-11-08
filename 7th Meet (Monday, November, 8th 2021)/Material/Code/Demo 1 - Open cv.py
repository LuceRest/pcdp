# ----------| Resize |----------

import cv2

img = cv2.imread('messi5.jpg')
cv2.imshow('messi_ori', img)

res = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('messi_resize', res)
cv2.waitKey()
cv2.destroyAllWindows()
