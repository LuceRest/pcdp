import cv2 as cv
import numpy as np

blank = np.zeros((550,550,3),dtype='uint8')

# Membuat trapesium
trp1 = (175, 60)
trp2 = (185, 40)
trp3 = (220, 40)
trp4 = (230, 60)
cv.circle(blank, trp1, 0,(0,165,255), -1)
cv.circle(blank, trp2, 0,(0,165,255), -1)
cv.circle(blank, trp3, 0,(0,165,255), -1)
cv.circle(blank, trp4, 0,(0,165,255), -1)
trapsm = np.array([trp1, trp2, trp3, trp4])
cv.drawContours(blank,[trapsm], 0, (0,165,255), -1)

# Membuat segitiga depan
trl1 = (50, 245)
trl2 = (125,245)
trl3 = (125, 150)
cv.circle(blank,trl1, 0, (0, 0, 255), -1)
cv.circle(blank,trl2, 0, (0, 0, 255), -1)
cv.circle(blank,trl3, 0, (0, 0, 255), -1)
triangle = np.array([trl1,trl2,trl3])
cv.drawContours(blank, [triangle], 0, (255,0,255), -1)


# Membuat badan
cv.rectangle(blank, (125,150),(370, 245), (145,40,44), -1)

# Membuat kepala 
cv.rectangle(blank, (480, 65), (370, 245),(53,38,122), -1)

# Membuat jendela
cv.rectangle(blank, (470, 80), (380,150), (192,192,192), -1)

# Membuat cerobong
cv.rectangle(blank, (185, 80), (220, 150), (105, 105, 105), -1)

# Membuat cerobong atas
cv.rectangle(blank, (175, 60), (230, 80), (0, 200, 0), -1)

# Membuat roda depan
cv.circle(blank, (blank.shape[1]//3, blank.shape[0]//2), 30, (105, 105, 105), -1)

# Membuat roda tengah
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 30, (105, 105, 105), -1)

# Membuat roda belakang besar
cv.circle(blank, (425, 260), 50, (105, 105, 105), -1)

# Membuat roda belakang kecil
cv.circle(blank, (425, 260), 35, (0,0,0), -1)

# Membuat garis roda pas
cv.line(blank, (170, 275), (430, 275), (0, 0, 128), 15)

# Membuat nama
cv.putText(blank, "Arieska Restu Harpian Dwika", (225,425), cv.FONT_HERSHEY_COMPLEX, .5, (255,210,162), 1)



cv.imshow("Kereta", blank)
cv.waitKey()