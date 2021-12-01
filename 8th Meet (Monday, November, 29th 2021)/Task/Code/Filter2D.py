import cv2
import numpy as np



img = cv2.imread('8th Meet (Monday, November, 29th 2021)\Task\Resource\lena.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# m, n = img.shape

# m, n = m-507, n-507
# cut = img[0:m, 0:n]
cut = img[0:5, 0:5]
print(f'\ncut : {cut}')


mask = np.array(
        [
        [0, -1, 0],
        [-1,5, -1],
        [0, -1, 0],
        ],
        dtype='float')

cv2.imshow('img original', img)

imgFilter = cv2.filter2D(img, -1, mask)
cv2.imshow('img filter', imgFilter)

# imgFilter = cv2.filter2D(img, -1, mask, anchor=(0,0))
# cv2.imshow('img filter 0,0', imgFilter)

# m, n = imgFilter.shape

# m, n = m-507, n-507
# cut = imgFilter[0:m, 0:n]
cutFilter = imgFilter[0:5, 0:5]
print(f'\ncutFilter : {cutFilter}')


cv2.waitKey(0)
cv2.destroyAllWindows()