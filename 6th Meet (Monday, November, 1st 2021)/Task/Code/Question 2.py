import cv2

# Reading image file
img = cv2.imread('6th Meet (Monday, November, 1st 2021)\Task\Resource\mountain.jpg')
cv2.imshow('ori.jpg', img)
cv2.waitKey(0)

# Applying NumPy scalar multiplication on image
fimg = cv2.divide(img, 1.5)


# Saving the output image
cv2.imwrite('darkerLib.jpg', fimg)
img_result = cv2.imread('darkerLib.jpg')
cv2.imshow('result.jpg', img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()