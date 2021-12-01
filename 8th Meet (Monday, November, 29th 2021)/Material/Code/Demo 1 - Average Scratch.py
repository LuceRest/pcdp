# Low Pass SPatial Domain Filtering
# to observe the blurring effect
import cv2
import numpy as np

# Read the image
img = cv2.imread('8th Meet (Monday, November, 29th 2021)\Material\Resource\sample.png', 0)

# Obtain number of rows and columns of the image
m, n = img.shape
print("Image dimens", img.shape)

# Averaging filter(3, 3) mask
mask = np.ones([3, 3], dtype=int)
mask = mask / 9
# print(f'mask : {mask}')

# Convolve the 3X3 mask over the image
img_new = np.zeros([m, n])

for i in range(1, m-1):
    for j in range(1, n-1):
        temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2] + \
            img[i, j-1]*mask[1, 0] + img[i, j]*mask[1, 1]+img[i, j+1]*mask[1, 2] + \
            img[i+1, j-1]*mask[2, 0]+img[i+1, j]*mask[2, 1]+img[i+1, j + 1]*mask[2, 2]

        img_new[i, j] = temp

img_new = img_new.astype(np.uint8)
m, n = img.shape
print("Image dimens", img_new.shape)

cv2.imwrite('8th Meet (Monday, November, 29th 2021)\Material\Resource\sample_filter.jpg', img_new)
