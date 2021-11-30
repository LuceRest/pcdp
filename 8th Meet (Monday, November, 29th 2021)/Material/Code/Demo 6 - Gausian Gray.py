import cv2
from matplotlib import pyplot as plt

image = cv2.imread('images/lena.jpg') # reads the image
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
figure_size = 9
new_image_gauss = cv2.GaussianBlur(image2, (figure_size, figure_size),0)

plt.figure(figsize=(11,6))
plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(new_image_gauss, cmap='gray'),plt.title('Gaussian Filter')
plt.xticks([]), plt.yticks([])
plt.show()
