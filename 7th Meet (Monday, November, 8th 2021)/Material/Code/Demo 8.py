import cv2 as cv

img1 = cv.imread('night_sky.jpeg')
print('size nigh_sky:', img1.shape)

img2 = cv.imread('moon.jpeg')
print('size moon:', img2.shape)

img_2_shape = img2.shape
roi = img1[0:img_2_shape[0], 0:img_2_shape[1]]
print('size roi:', roi.shape)

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Now black-out the area of moon in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
print(img1.shape, mask.shape)

# Take only region of moon from moon image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask)

# Put moon in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)

img1[0:img_2_shape[0], 0:img_2_shape[1]] = dst
# Create resizable windows for our display images

cv.imshow('mask', mask)
cv.imshow('maskinv', mask_inv)
cv.imshow('img1_bg', img1_bg)
cv.imshow('img2_fg', img2_fg)
cv.imshow('res', img1)


if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
