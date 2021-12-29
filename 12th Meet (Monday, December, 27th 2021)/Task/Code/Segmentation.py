import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("12th Meet (Monday, December, 27th 2021)\Task\Resource\czech_coin.jpg")
roi = image[0:500, 0:500]

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Image blur : Gaussian blur
k = 15
imgBlur = cv2.GaussianBlur(imgGray, (k, k), 0)

# Threshold image
thresh = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)

# kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

# Morphology
imgErode = cv2.erode(thresh, kernel, iterations=2)
imgClosing = cv2.morphologyEx(imgErode, cv2.MORPH_CLOSE, kernel, iterations=6)
imgDilate = cv2.dilate(imgClosing, kernel, iterations=2)

contImg = imgDilate.copy()
contours, hierarchy = cv2.findContours(contImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)

    if area < 100:
        continue
    if len(cnt) < 0:
        continue

    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(roi, ellipse, (0,255,0), 2)

# Resize image
imgGray = cv2.resize(imgGray, (0,0), None, 0.5, 0.5)
imgBlur = cv2.resize(imgBlur, (0,0), None, 0.5, 0.5)
thresh = cv2.resize(thresh, (0,0), None, 0.5, 0.5)
imgErode = cv2.resize(imgErode, (0,0), None, 0.5, 0.5)
imgClosing = cv2.resize(imgClosing, (0,0), None, 0.5, 0.5)
imgDilate = cv2.resize(imgDilate, (0,0), None, 0.5, 0.5)

# Stacking image
hStack1 = np.hstack([imgGray, imgBlur, thresh])
hStack2 = np.hstack([imgErode, imgClosing, imgDilate])
vStack = np.vstack([hStack1, hStack2])

cv2.imshow('Stages', vStack)
cv2.imshow('Result', roi)

cv2.waitKey(0)


# plt.figure(figsize=(12, 6))
# plt.title("Result"), plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
# plt.show()
