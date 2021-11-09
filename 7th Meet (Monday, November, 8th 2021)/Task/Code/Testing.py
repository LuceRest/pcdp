import cv2 as cv

img1 = cv.imread('7th Meet (Monday, November, 8th 2021)\Task\Resource\cloudy-city-resize.jpg')
print('size cloud-city:', img1.shape)

img2 = cv.imread('7th Meet (Monday, November, 8th 2021)\Task\Resource\jet-resize.jpg')
print('size jet-resize:', img2.shape)

img_2_shape = img2.shape
roi = img1[0:img_2_shape[0], 0:img_2_shape[1]]
print('size roi:', roi.shape)

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 145, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Now black-out the area of moon in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask)
print(img1.shape, mask.shape)

# Take only region of moon from moon image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask_inv)

# Put moon in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)

img1[0:img_2_shape[0], 0:img_2_shape[1]] = dst
# Create resizable windows for our display images

cv.imshow('1', mask)
cv.imshow('2', mask_inv)
cv.imshow('3', img1_bg)
cv.imshow('4', img2_fg)
cv.imshow('res', img1)


if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
