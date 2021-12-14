import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread("img/sample.png", 0)

m, n = image.shape

k = 5 # 3, 5, 7, 9
kernel = np.ones((k,k), dtype=np.uint8)
constant = (k-1) // 2
print(constant)


# array nol
imgErosi = np.zeros((m,n), dtype=np.uint8)


for i in range(constant, m-constant): # (2, m-2)
    for j in range(constant, n-constant): #(2, n-2)
        temp = image[i-constant:i+constant+1, j-constant:j+constant+1]
        product = temp * kernel
        imgErosi[i,j] = np.min(product)


plt.figure(figsize=(15,7))
plt.subplot(121),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgErosi,cmap = 'gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])
plt.show()
