import numpy as np
import cv2
from matplotlib import pyplot as plt


image2 = cv2.imread("img/sample-text.png", 0)

m, n = image2.shape

imgDilasi= np.zeros((m, n), dtype=np.uint8)

kernel = np.array([[0,1,0], [1,1,1],[0,1,0]])
constant1 = 1

for i in range(constant1, m-constant1):
    for j in range(constant1, n-constant1):
        temp = image2[i-constant1:i+constant1+1, j-constant1:j+constant1+1]
        product = temp * kernel
        imgDilasi[i,j] = np.max(product)


plt.figure(figsize=(15,7))
plt.subplot(121),plt.imshow(image2,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgDilasi,cmap = 'gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])
plt.show()
