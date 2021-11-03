# 5200411488 - Arieska Restu Harpian Dwika

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


def browseImage():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("JPG File", "*.jpg"), 
                                        ("PNG File", "*.png"), 
                                        ("All Files", "*.*"))
                                    )

    img = Image.open(fln)
    imgTk = ImageTk.PhotoImage(img)
    lblImg.configure(image=imgTk)
    lblImg.image = imgTk


def opencv2Tkinter(img):
    imgPill = Image.fromarray(img)
    imgTkinter = ImageTk.PhotoImage(imgPill)
    return imgTkinter


def clipping(intensity):
    if intensity < 0:
        return 0
    if intensity > 255:
        return 255
    return intensity

def brightening():
    global fln
    
    img = Image.open(fln)
    px = img.load()

    horizontal = img.size[0]
    vertical = img.size[1]

    for x in range(horizontal):
        for y in range(vertical):
            r = clipping(px[x, y][0] + int(valBright.get()))
            g = clipping(px[x, y][1] + int(valBright.get()))
            b = clipping(px[x, y][2] + int(valBright.get()))
            px[x, y] = (r, g, b)

    imgTk = ImageTk.PhotoImage(img)
    lblImg.configure(image=imgTk)
    lblImg.image = imgTk



if __name__ == '__main__':
    root = Tk()
    fln = None

    frmBtn = Frame(root)
    frmBtn.pack(side=BOTTOM, padx=15, pady=15)

    lblImg = Label(root)
    lblImg.pack()

    btn = Button(frmBtn, text="Browser Image", background="lightblue", activebackground='#0275D8', padx=2, pady=2, font="Normal 10",cursor="hand2", command=browseImage)
    btn.grid(row=0, column=0)

    btnExit = Button(frmBtn, text="Exit", background="#F47174", activebackground='red', padx=4, pady=2, font="Normal 10",cursor="hand2", command=lambda: exit())
    btnExit.grid(row=0, column=2)

    txtBinary = Label(frmBtn, text="Value Bright", font="Normal 10")
    txtBinary.grid(row=1, column=0)

    valBright = Entry(frmBtn, font="Normal 10", bd=3)
    valBright.grid(row=1, column=1)
    
    btnBright = Button(frmBtn, text="Brightening", background="lightblue", activebackground='#0275D8', padx=2, pady=2, font="Normal 10",cursor="hand2", command=brightening)
    btnBright.grid(row=1, column=2)
    
    # sliderBinary = Scale(frmBtn, from_=0, to=255, orient=HORIZONTAL, length=255, cursor="hand2", command=rgb2BinarySlider)
    # sliderBinary.grid(row=2, column=0, columnspan=5)
    

    root.title("Image Browser App - 5200411488")
    root.geometry("1280x720")
    root.mainloop()