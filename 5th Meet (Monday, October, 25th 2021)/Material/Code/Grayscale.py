# Convert RGB to Grayscale (from scratch)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb_to_gray(img):
        grayImage = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R * .299)
        G = (G * .587)
        B = (B * .114)

        Avg = (R+G+B)
        print(Avg)
        grayImage = img.copy()

        for i in range(3):
           grayImage[:,:,i] = Avg
           
        return grayImage       

image = mpimg.imread("mountain.jpg")   
grayImage = rgb_to_gray(image) 
plt.imshow(grayImage)
# plt.show()


image = cv2.imread("mountain.jpg")
grayImage = rgb_to_gray(image)  

cv2.imwrite("5th Meet (Monday, October, 25th 2021)\Material\Resource\scratch_grayscale.jpg", grayImage)



plt.imshow(grayImage)
plt.show()