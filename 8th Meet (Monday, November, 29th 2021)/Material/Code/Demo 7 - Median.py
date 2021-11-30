import cv2
from matplotlib import pyplot as plt

image = cv2.imread('images/lena.jpg')  # reads the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
figure_size = 9
new_image = cv2.medianBlur(image, figure_size)

plt.figure(figsize=(11, 6))
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_HSV2RGB)),plt.title('Median Filter')
plt.xticks([]), plt.yticks([])
plt.show()
