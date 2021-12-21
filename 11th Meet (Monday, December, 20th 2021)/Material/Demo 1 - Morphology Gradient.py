import cv2
import numpy as np
import os
import matplotlib as plt

''' Morphology Gradient '''
image = cv2.imread("img/sample.jpg", 0)
k = 3
kernelSize = (k, k)

# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)

# Image Process
imgGradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

plt.figure(figsize=(21, 7))
plt.subplot(121), plt.title("Original"), plt.imshow(image, cmap="gray")
plt.subplot(122), plt.title("Morph Gradient"), plt.imshow(imgGradient, cmap="gray")
plt.show()
