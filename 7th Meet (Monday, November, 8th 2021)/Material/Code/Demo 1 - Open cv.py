# ----------| Resize |----------

import cv2

img = cv2.imread('7th Meet (Monday, November, 8th 2021)\Task\Resource\jet.jpg')
cv2.imshow('jet_ori', img)

res = cv2.resize(img, None, fx=.1, fy=.1, interpolation=cv2.INTER_CUBIC)
cv2.imshow('jet_resize', res)
cv2.imwrite('jet-resize.jpg',res)
cv2.waitKey()
cv2.destroyAllWindows()
