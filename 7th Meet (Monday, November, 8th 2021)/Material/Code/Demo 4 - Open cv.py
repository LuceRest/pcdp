# ----------| Flip |----------


import cv2

img = cv2.imread('lena.jpg')
cv2.imshow('lena_ori', img)
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
# (225, 400, 3)

img_flip_ud = cv2.flip(img, 0)
cv2.imshow('lena_flip0_vertically', img_flip_ud)
# True

img_flip_lr = cv2.flip(img, 1)
cv2.imshow('lena_flip>0_horizontally', img_flip_lr)
# True

img_flip_ud_lr = cv2.flip(img, -1)
cv2.imshow('lena_flip<0_verhoriz', img_flip_ud_lr)
# True
cv2.waitKey(0)
cv2.destroyAllWindows()
