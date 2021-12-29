import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("12 Meet (Monday, December, 27th 2021)\Material\Resource\image_gray.png")
roi = image[0:500, 0:500]

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Image blur : Gaussian blur
k = 15
img_blur = cv2.GaussianBlur(img_gray, (k, k), 0)

# Threshold image
thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)


# kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

# Morphology
img_erode = cv2.erode(thresh, kernel, iterations=2)
img_closing = cv2.morphologyEx(img_erode, cv2.MORPH_CLOSE, kernel, iterations=6)
img_dilasi = cv2.dilate(img_closing, kernel, iterations=2)

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.title("Grayscale"), plt.imshow(thresh, cmap="gray")
plt.subplot(122), plt.title("Closing"), plt.imshow(img_closing, cmap="gray")

plt.figure(figsize=(18, 6))
plt.subplot(131), plt.title("Threshold"), plt.imshow(thresh, cmap="gray")
plt.subplot(132), plt.title("Closing"), plt.imshow(img_closing, cmap="gray")
plt.subplot(133), plt.title("Dilasi"), plt.imshow(img_dilasi, cmap="gray")
plt.show()
