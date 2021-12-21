# Importing OpenCV and numpy
import cv2

# Defining the kernel to be used in Top-Hat
filterSize =(12,5)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,
								filterSize)

# Reading the image named 'input.jpg'
input_image = cv2.imread("lena.png")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Applying the Black-Hat operation
tophat_img = cv2.morphologyEx(input_image,
							cv2.MORPH_BLACKHAT,
							kernel)

cv2.imshow("original", input_image)
cv2.imshow("tophat", tophat_img)
cv2.waitKey(5000)
