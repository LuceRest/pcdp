import cv2 as cv

""" ------------------------------------------------------------------------------
    Resize Citra
------------------------------------------------------------------------------ """
img = cv.imread('3rd Meet (Monday, October, 11th 2021)/Practice/resources/messi_large.jpg', cv.IMREAD_UNCHANGED)

""" 'shape' untuk mendapatkan dimensi citra """
print('Original Dimensions : ', img.shape)

scale_percent = 50  # Scale 50% dari dimensi asli
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
""" Dimensi baru """
dim = (width, height)

""" 'resize' untuk mengubah dimensi citra """
resized = cv.resize(img, dim, interpolation=cv.INTER_BITS)

print('Resized Dimensions : ', resized.shape)

""" Buat file baru dari dimensi yang baru """
cv.imwrite('3rd Meet (Monday, October, 11th 2021)/Practice/resources/messi_new.jpg', resized)

cv.imshow("Resized image", resized)
cv.waitKey(0)
cv.destroyAllWindows()

# """ ------------------------------------------------------------------------------
#     Menempel objek ke Citra
# ------------------------------------------------------------------------------ """
# img = cv.imread('3rd Meet (Monday, October, 11th 2021)/Practice/resources/messi_new.jpg', cv.IMREAD_COLOR)

# print(img.shape)

# cv.imshow('Messi Kick', img)
# cv.waitKey(0)
# # cv.destroyAllWindows()

# """
# Ambil objek bola pada pixel [32:139, 233:342]
# 32:139  -> Dari baris 32 sampai baris 139
# 233:342 -> Dari kolom 233 sampai kolom 342
# """
# # Titik awal    -> 233, 32
# # Titik akhir   -> 342, 139
# ball = img[32:139, 233:342]
# print(ball.dtype)
# print(ball.shape)

# """ Menempel objek bola pada pixel [155:262, 409:518] """
# img[155:262, 409:518] = ball


# """ Buat file baru dengan objek yang ditempel """
# cv.imwrite('3rd Meet (Monday, October, 11th 2021)/Practice/resources/messi_new_doubleball.jpg', img)

# cv.imshow('Messi Kick', img)
# cv.waitKey(0)
# cv.destroyAllWindows()