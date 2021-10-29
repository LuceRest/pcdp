import cv2 as cv

# img = cv.imread('resources/cat.jpg')
# cv.imshow('Picture of Cat', img)
#
# cv.waitKey(0)



# section-2


# capture = cv.VideoCapture('resources/kitten.mp4')
#
# while True:
#     isTrue, frame = capture.read()
#
#     # if cv.waitKey(20) & 0xFF==ord('d'):
#     # This is the preferred way - if `isTrue` is false (the frame could
#     # not be read, or we're at the end of the video), we immediately
#     # break from the loop.
#     if isTrue:
#         cv.imshow('Video', frame)
#         if cv.waitKey(20) & 0xFF==ord('d'):
#             break
#     else:
#         break
#
# capture.release()
# cv.destroyAllWindows()




# section-3


import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 255,0,255
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Donny!!!', (10,225), cv.FONT_HERSHEY_DUPLEX,
           1.0, (255,255,0), 1)
cv.imshow('Text', blank)

cv.waitKey(0)




# section-4


# import cv2 as cv
# import numpy as np

# image = np.ones((300, 300, 3), np.uint8) * 255

# pt1 = (150, 100)
# pt2 = (100, 200)
# pt3 = (200, 200)

# cv.circle(image, pt1, 1, (0,255,0), -1)
# cv.circle(image, pt2, 1, (0,255,0), -1)
# cv.circle(image, pt3, 1, (0,255,0), -1)


# triangle_cnt = np.array( [pt1, pt2, pt3] )

# cv.drawContours(image, [triangle_cnt], 0, (0,255,0), -1)

# cv.imshow("image", image)
# cv.waitKey()