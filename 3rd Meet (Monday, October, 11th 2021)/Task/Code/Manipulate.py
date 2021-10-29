import cv2 as cv


img = cv.imread('3rd Meet (Monday, October, 11th 2021)\Task\Resources\soccer_kid_small.JPG', cv.IMREAD_UNCHANGED)
width, height = 488, 325
img = cv.resize(img, (width, height))
print(img.shape)

cv.imshow('Kid Kick', img)
cv.waitKey(0)

# Mengambil objek bola

# Titik awal -> 266, 253 | Titik akhir -> 304, 291
ball = img[253:291, 266:304]
print(ball.dtype)
print(ball.shape)

# Menaruh objek bola

# Titik awal -> 25, 273 | Titik akhir -> 63, 311
img[273:311, 25:63] = ball

# Menaruh NPM

# Titik awal -> 380, 271 | Titik akhir -> 480, 302 | Titik pas (titik c) -> 383,290
cv.putText(img, "5200411488", (383,290), cv.FONT_HERSHEY_COMPLEX, .475, (75,57,44), 1)

# Membuat file baru

cv.imwrite('3rd Meet (Monday, October, 11th 2021)\Task\Resources\soccer_kid_small_doubleBall.JPG', img)

cv.imshow('Kid Kick', img)
cv.waitKey(0)
cv.destroyAllWindows()