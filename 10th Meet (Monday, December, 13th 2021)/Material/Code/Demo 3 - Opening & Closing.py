import numpy as np
import cv2
from matplotlib import pyplot as plt


#Function for erosion
def erosi(img, kernel):
    imgErode = cv2.erode(img, kernel, iterations= 1)
    return imgErode

#Function for dilation
def dilasi(img, kernel):
    imgDilate = cv2.dilate(img, kernel, iterations= 1)
    return imgDilate


# Read image
img = cv2.imread("img/finger.png", 0)

# Kernel
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))


# -----------| Opening (Erosi -> Dilasi) |-----------

# Image -> Erosi
imgAeB = erosi(img, se)

# Image erosi -> dilasi
imgAoB = dilasi(imgAeB, se)


# -----------| Closing (Dilasi -> Erosi) |-----------

# Image dilasi -> dilasi
imgAoBdB = dilasi(imgAoB, se)

# Image dd -> erosi
imgAoBdBeB= erosi(imgAoBdB, se)

plt.figure(figsize=(15,7))
plt.subplot(231),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(imgAeB,cmap = 'gray')
plt.title('Erosi'), plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(imgAoB,cmap = 'gray')
plt.title('Dilasi'), plt.xticks([]), plt.yticks([])

plt.subplot(234),plt.imshow(imgAoBdB,cmap = 'gray')
plt.title('Dilasi'), plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(imgAoBdBeB,cmap = 'gray')
plt.title('Dilasi'), plt.xticks([]), plt.yticks([])
plt.show()

