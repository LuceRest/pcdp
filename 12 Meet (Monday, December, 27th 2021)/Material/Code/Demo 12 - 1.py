import numpy as np
import cv2
import matplotlib.pyplot as plt


image = cv2.imread("coin_dataset/image_gray.png")
roi = image[0:500, 0:500]

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


plt.figure(figsize=(12, 6))
plt.title("Grayscale"), plt.imshow(img_gray, cmap="gray")
plt.show()


