import cv2
import numpy as np
import os
import matplotlib as plt


image = cv2.imread("img/sample.jpg", 0)



''' Morphology Black hat '''
k = 7 # Semakin besar kernel, semakin jelas object nya
kernelSize = (k, k)

# Structuring Element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)

# Image process
# Blackhat = hasil closing - image
imgBlackhat = closing(image, kernel) - image

plt.figure(figsize=(21, 7))
plt.subplot(121), plt.title("Original"), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.title("Morph Black Hat"), plt.imshow(imgBlackhat, cmap="gray")
plt.show()
