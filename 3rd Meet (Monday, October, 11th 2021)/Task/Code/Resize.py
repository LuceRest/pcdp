import cv2 as cv


img = cv.imread('3rd Meet (Monday, October, 11th 2021)\Task\Resources\soccer_kid_large.JPG', cv.IMREAD_UNCHANGED)
print('Original Dimensions : ', img.shape)

# Meresize gambar

scalePercent = 60 
width = int(img.shape[1] * scalePercent / 100)
height = int(img.shape[0] * scalePercent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation=cv.INTER_BITS)
print('Resized Dimensions : ', resized.shape)

# Membuat file baru

cv.imwrite('3rd Meet (Monday, October, 11th 2021)\Task\Resources\soccer_kid_small.JPG', resized)

cv.imshow("Resized image", resized)
cv.waitKey(0)

cv.destroyAllWindows()