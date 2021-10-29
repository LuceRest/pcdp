import cv2
import numpy as np


fln = "mountain.jpg"

# Read color image
img = cv2.imread(fln)

# Get the image's height, width, and channels
height, width, channels = img.shape

# Create blank Binary Image
img_binary = np.zeros((height,width,1))

# Create grayscale image
img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set Threshold
thresh = 120

for i in np.arange(height):
    for j in np.arange(width):
        x = img_grayscale.item(i,j)
        if x >= thresh:
            y = 1
        else :
            y = 0

        img_binary.itemset((i,j,0),int(y))


print(f'\n\n{img_binary}\n\n')

cv2.imshow("Binary", img_binary)

cv2.waitKey(0)

cv2.destroyAllWindows()