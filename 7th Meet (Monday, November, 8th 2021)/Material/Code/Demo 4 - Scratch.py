# ----------| Flip |----------


import cv2
import numpy as np


def flipv(imgg, h, w):
    img2 = np.zeros([h, w, 3], np.uint8)
    for i in range(h):
        img2[i, :] = imgg[h-i-1, :]

    return img2


img = cv2.imread("lena.jpg", -1)
print(img.shape)
rows, cols, rgb = img.shape

ads = flipv(img, rows, cols)

cv2.imshow("qw", ads)

cv2.waitKey(0)
cv2.destroyAllWindows()
