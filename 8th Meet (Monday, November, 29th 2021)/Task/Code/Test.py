# Low Pass SPatial Domain Filtering
# to observe the blurring effect
import cv2
import numpy as np

# Read the image
img = cv2.imread('8th Meet (Monday, November, 29th 2021)\Task\Resource\lena.jpg', 0)

# Obtain number of rows and columns of the image
m, n = img.shape

print("Image dimens", img.shape)

m, n = m-507, n-507
cut = img[0:m, 0:n]
print(f"\nm : {m}")
print(f"\nn : {n}")
print(f'\nimg : {img}')
print(f'\ncut : {cut}')
t = cut[-1, -1]     # Pucuk bawah
print(f't : {t}')


# Averaging filter(3, 3) mask
mask = np.array(
        [
        [0, -1, 0],
        [-1,5, -1],
        [0, -1, 0],
        ],
        dtype='float')
print(f'\nmask : {mask}')

# Convolve the 3X3 mask over the image
img_new = np.zeros([m, n])

for i in range(1, m):
    for j in range(1, n):
        p = img[i-1, j-1]
        print(f'\nimg[i-1, j-1 : ')
        print(p)
        # if 
        temp = img[i-1, j-1]*mask[0, 0] + img[i-1, j]*mask[0, 1] + img[i-1, j + 1]*mask[0, 2] + \
            img[i, j-1]*mask[1, 0] + img[i, j]*mask[1, 1] + img[i, j+1]*mask[1, 2] + \
            img[i+1, j-1]*mask[2, 0] + img[i+1, j]*mask[2, 1] + img[i+1, j + 1]*mask[2, 2]

        img_new[i, j] = temp

img_new = img_new.astype(np.uint8)
m, n = img_new.shape
print("\nImage dimens", img_new.shape)
print(f"\nm : {m}")
print(f"\nn : {n}")
print(f'\nnew image : {img_new}')

cv2.imwrite('8th Meet (Monday, November, 29th 2021)\Task\Resource\lena_filter.jpg', img_new)
