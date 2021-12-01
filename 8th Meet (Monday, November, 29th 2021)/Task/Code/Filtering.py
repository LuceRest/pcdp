# 5200411488 - Arieska Restu Harpian Dwika

import cv2
import numpy as np
import os
from tkinter import *
from tkinter import font
from tkinter import filedialog
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
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
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgPill = Image.fromarray(img)
    return imgPill
    
def resizeImg(img, width, height):
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
    return img

def browseImage():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("All Files", "*.*",),
                                        ("PNG File", "*.png"), 
                                        ("JPG File", "*.jpg"))
                                    )
    
    img = opencv2Pill(resizeImg(cv2.imread(fln), 512, 512))
    setOriginal(img)

def filtering():
    global fln
    
    img = cv2.imread(fln)

    kernel = np.array(
            [
            [0, -1, 0],
            [-1,5, -1],
            [0, -1, 0],
            ],
            dtype='float')

    imgFilter = cv2.filter2D(img, -1, kernel)
    
    setResult(opencv2Pill(resizeImg(imgFilter, 512, 512)))
    


if __name__ == '__main__':
    style = Style()
    window = style.master


    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)

    frmImg = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
    frmImg.grid(row=0, column=0, padx=20, pady=20)

    frmImgOri = ttk.Frame(frmImg, style='info.TFrame', width=512, height=512)
    frmImgOri.pack_propagate(0)
    frmImgOri.pack(side="left", padx=20, pady=30)

    frmBtn = ttk.Frame(frmImg, style='secondary.TFrame', width=100, height=200)
    frmBtn.pack(side="left", padx=20, pady=30)

    frmImgResult = ttk.Frame(frmImg, style='info.TFrame', width=512, height=512)
    frmImgResult.pack_propagate(0)
    frmImgResult.pack(side="left", padx=20, pady=20)

    btnBrowse = ttk.Button(frmBtn, text='Browse Image', style='info.TButton', cursor="hand2", width=12, command=browseImage)
    btnBrowse.pack(side='top', pady=10)

    btnFilter = ttk.Button(frmBtn, text='Filter', style='success.TButton', cursor="hand2", width=12, command=filtering)
    btnFilter.pack(side='top', pady=10)

    btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2", width=12, command=lambda: exit())
    btnExit.pack(side='top', pady=10)

    lblOriImg = ttk.Label(frmImgOri)
    lblResultImg = ttk.Label(frmImgResult)

    window.title("Image Filtering - 5200411488")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.mainloop()


