# ----------| Bitwise Not |----------


import numpy as np
import cv2

# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# draw a circle
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)


bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT Circ", bitwiseNot)

bitwiseNot = cv2.bitwise_not(rectangle)
cv2.imshow("NOT rECT", bitwiseNot)


cv2.waitKey(0)
cv2.destroyAllWindows()
