# ----------| Bitwise XOR |----------


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


bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Rect XOR Circ", bitwiseXor)


cv2.waitKey(0)
cv2.destroyAllWindows()
