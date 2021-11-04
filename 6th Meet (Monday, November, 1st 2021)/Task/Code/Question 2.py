import cv2

# Reading image file
img = cv2.imread('lena.png')
cv2.imshow('ori.jpg', img)
cv2.waitKey(0)

print(f'\nImg : {img}\n---------------')

# Applying NumPy scalar multiplication on image

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(f'\nImgRGB : {imgRGB}\n---------------')

fimg = cv2.divide(imgRGB, 0.9)
cv2.imshow('result.jpg', fimg)
print(f'\nfimg : {fimg}\n---------------')


# Saving the output image
# cv2.imwrite('darkerLib.jpg', fimg)
# img_result = cv2.imread('darkerLib.jpg')


cv2.waitKey(0)
cv2.destroyAllWindows()