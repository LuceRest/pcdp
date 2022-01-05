import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("13th Meet (Monday, January, 3rd 2022)/Responsi/Resource/responsi2022.jpg")
roi = image[0:697, 0:500]

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

# Draw Contour
for cnt in contours:
    area = cv2.contourArea(cnt)

    if area < 100:
        continue
    if len(cnt) < 0:
        continue

    ellipse = cv2.fitEllipse(cnt)
    x = int(ellipse[0][0])-20
    y = int(ellipse[0][1])+10
    if area >= 4500 and area <= 5000:       # Rp 100
        cv2.ellipse(roi, ellipse, (255,0,0), 2)
        cv2.putText(roi, '100', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
    elif area > 5000 and area < 5500:       # Rp 500 perunggu
        cv2.ellipse(roi, ellipse, (255,255,0), 2)
        cv2.putText(roi, '500', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
    elif area >= 5500 and area <= 6000:     # Rp 200
        cv2.ellipse(roi, ellipse, (255,0,255), 2)
        cv2.putText(roi, '200', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
    elif area > 6000 and area <= 7000:      # Rp 500 perak
        cv2.ellipse(roi, ellipse, (0,255,0), 2)
        cv2.putText(roi, '500', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
    else:   
        # print(f'area {num} : {area}\n') 
        cv2.ellipse(roi, ellipse, (0,0,255), 2)

# Resize image
imgGray = cv2.resize(imgGray, (0,0), None, 0.5, 0.5)
imgBlur = cv2.resize(imgBlur, (0,0), None, 0.5, 0.5)
thresh = cv2.resize(thresh, (0,0), None, 0.5, 0.5)
imgErode = cv2.resize(imgErode, (0,0), None, 0.5, 0.5)
imgClosing = cv2.resize(imgClosing, (0,0), None, 0.5, 0.5)
imgDilate = cv2.resize(imgDilate, (0,0), None, 0.5, 0.5)

imgResult = cv2.resize(roi, (0,0), None, 0.5, 0.5)

# Stacking image
hStack1 = np.hstack([imgGray, imgBlur, thresh])
hStack2 = np.hstack([imgErode, imgClosing, imgDilate])
vStack = np.vstack([hStack1, hStack2])

cv2.imshow('Stages', vStack)
cv2.imshow('Result', roi)
cv2.imshow('imgResult', imgResult)

cv2.waitKey(0)
