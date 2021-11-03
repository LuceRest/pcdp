# 5200411488 - Arieska Restu Harpian Dwika

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


def setOriginal(img):
    imgTk = ImageTk.PhotoImage(img)
    lblOriImg.configure(image=imgTk)
    lblOriImg.image = imgTk
    lblOriImg.pack()


def setResult(img):
    imgTk = ImageTk.PhotoImage(img)
    lblResultImg.configure(image=imgTk)
    lblResultImg.image = imgTk
    lblResultImg.pack()


def opencv2Pill(img):
    imgPill = Image.fromarray(img)
    # imgTkinter = ImageTk.PhotoImage(imgPill)
    return imgPill

def resizeImg(img):
    width, height = 600, 512
    img = cv2.resize(img, (width, height))
    return img


def clipping(intensity):
    if intensity < 0:
        return 0
    if intensity > 255:
        return 255
    return intensity


def browseImage():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("JPG File", "*.jpg"), 
                                        ("PNG File", "*.png"), 
                                        ("All Files", "*.*"))
                                    )

    img = Image.open(fln)
    setOriginal(img)


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
    
    setResult(img)


def brighteningSlider(e):
    global fln
    
    img = cv2.imread(fln)

    valBright = int(sldBright.get())
    # m = np.ones(img.shape, dtype='uint8') * valBright
    imgBright = cv2.add(img, valBright)
    imgTk = opencv2Pill(imgBright)
    setResult(imgTk)

    # print(f'\n{int(sldBright.get())}\n')


if __name__ == '__main__':
    fln = None
    style = Style()
    window = style.master


    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)

    frmImgOri = ttk.Frame(frm, style='secondary.TFrame', width=600, height=512)
    frmImgOri.pack_propagate(0)
    frmImgOri.grid(row=0, column=0, padx=20, pady=30)

    frmImgRes = ttk.Frame(frm, style='secondary.TFrame', width=600, height=512)
    frmImgRes.pack_propagate(0)
    frmImgRes.grid(row=0, column=1, padx=20, pady=30)

    frmBtn = ttk.Frame(frm, style='primary.TFrame', width=1000, height=100)
    # frmImgRes.pack_propagate(0)
    frmBtn.grid(row=1, column=0, columnspan=2, pady=20)

    lblOriImg = ttk.Label(frmImgOri)
    # lblOriImg.pack()

    lblResultImg = ttk.Label(frmImgRes, style='info.TLabel')
    # lblResultImg.grid(row=0, column=0)

    btnBrowse = ttk.Button(frmBtn, text='Browse Image', style='info.TButton', cursor="hand2", command=browseImage)
    btnBrowse.grid(row=0, column=0, columnspan=2, padx=15)

    btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2")
    btnExit.grid(row=0, column=2, columnspan=2, padx=20)

    valBright = ttk.Entry(frmBtn, style='info.TEntry')
    valBright.grid(row=1, column=0, columnspan=2, padx=15, pady=10)

    btnBright = ttk.Button(frmBtn, text='Brightening', style='info.TButton', cursor="hand2", command=brightening)
    btnBright.grid(row=1, column=2, columnspan=2, padx=20, pady=10)

    sldBright = ttk.Scale(frmBtn, from_=-255, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=511, command=brighteningSlider)
    sldBright.grid(row=2, column=0, columnspan=4, padx=20, pady=10)


    window.title("Image Browser App - 5200411488")
    window.geometry("1280x720")
    # window.resizable(0, 0)
    window.mainloop()


