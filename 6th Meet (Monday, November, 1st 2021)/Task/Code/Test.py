
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
from tkinter import filedialog
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
import os
from PIL import Image, ImageTk
    
img = cv2.imread("lena.png")

def bright(valBright):
    if valBright > 0:
        mtxBright = np.ones(img.shape, dtype="uint8") * valBright
        imgBright = cv2.add(img, mtxBright)
    elif valBright < 0:
        mtxBright = np.ones(img.shape, dtype="uint8") * abs(valBright)
        imgBright = cv2.subtract(img, mtxBright)

    cv2.imshow(f"Result : {valBright}", imgBright)


cv2.imshow("Src", img)
bright(150)
bright(-150)
cv2.waitKey()