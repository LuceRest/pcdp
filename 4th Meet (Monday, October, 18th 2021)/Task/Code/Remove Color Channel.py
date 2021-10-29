from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2 as cv


fln = None

def showImage():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("JPG File", "*.jpg"), 
                                        ("PNG File", "*.png"), 
                                        ("All Files", "*.*"))
                                    )
    print("Image path : ", fln)
    img = Image.open(fln)

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk

def showRed():
    global fln

    img = Image.open(fln)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            img.putpixel((x,y), (r, 0, 0))

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk

def showGreen():
    global fln

    img = Image.open(fln)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            img.putpixel((x,y), (0, g, 0))

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk

def showBlue():
    global fln

    img = Image.open(fln)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            img.putpixel((x,y), (0, 0, b))

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk


if __name__ == '__main__':
    root = Tk()

    frm = Frame(root)
    frm.pack(side=BOTTOM, padx=15, pady=15)

    lbl = Label(root)
    lbl.pack()

    btn = Button(frm, text="Browser Image", command=showImage)
    btn.pack(side=tk.LEFT)

    btn2 = Button(frm, text="Red", command=showRed)
    btn2.pack(side=tk.LEFT, padx=10)

    btn2 = Button(frm, text="Green", command=showGreen)
    btn2.pack(side=tk.LEFT, padx=10)

    btn2 = Button(frm, text="Blue", command=showBlue)
    btn2.pack(side=tk.LEFT, padx=10)

    btn2 = Button(frm, text="Exit", command=lambda: exit())
    btn2.pack(side=tk.LEFT, padx=10)


    root.title("Image Browser App")
    root.geometry("1280x720")
    root.mainloop()




