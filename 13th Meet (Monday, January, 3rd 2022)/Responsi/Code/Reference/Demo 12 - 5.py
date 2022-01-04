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


cont_img = img_dilasi.copy()
contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area < 1000 or area > 4000:
        continue
    if len(cnt) < 5:
        continue

    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(roi, ellipse, (0,255,0), 2)

plt.figure(figsize=(12, 6))
plt.title("Result"), plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.show()
