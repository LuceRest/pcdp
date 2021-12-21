import cv2
import numpy as np
import os
import matplotlib as plt


image = cv2.imread("img/sample.jpg", 0)


''' Morphology Top hat/White hat '''
k = 7 # Semakin besar kernel, semakin jelas object nya
kernelSize = (k, k)

# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)

# Image process
# Tophat = citra awal - hasil opening
imgTophat = image - opening(image, kernel)

plt.figure(figsize=(21, 7))
plt.subplot(121), plt.title("Original"), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.title("Morph Top Hat"), plt.imshow(imgTophat, cmap="gray")
plt.show()
