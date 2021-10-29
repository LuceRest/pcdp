import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


fln = "mountain.jpg"

imgCv = cv2.imread(fln)
imgImage = Image.open(fln)

# imgTkCv = ImageTk.PhotoImage(imgCv)
# imgTkImage = ImageTk.PhotoImage(imgImage)

print(f'\n{imgCv}\n----------------')
print(f'\n{imgImage}\n----------------')

# print(f'\n{imgTkCv}\n----------------')
# print(f'\n{imgTkImage}\n----------------')



cv2.waitKey(0)
cv2.destroyAllWindows()