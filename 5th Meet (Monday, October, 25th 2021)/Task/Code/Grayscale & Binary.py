import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
    

fln = None

def browseImage():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("JPG File", "*.jpg"), 
                                        ("PNG File", "*.png"), 
                                        ("All Files", "*.*"))
                                    )
    print("Image path : ", fln)
    img = Image.open(fln)

    print("\n\n{}\n\n".format(img))

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk


def rgb2Gray():
    global fln

    img = Image.open(fln)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            r = (r * .299)
            g = (g * .587)
            b = (b * .114)
            sum = int((r+g+b))
            img.putpixel((x,y), (sum, sum, sum))

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk


def rgb2Binary():
    global fln
    
    imgGrayscale = Image.open(fln).convert('L')
    pxGrayscale = imgGrayscale.load()

    horizontal = imgGrayscale.size[0]
    vertical = imgGrayscale.size[1]
    
    for x in range(horizontal):
        for y in range(vertical):
            if pxGrayscale[x, y] < int(thresh.get()):
                pxGrayscale[x, y] = 0
            else:
                pxGrayscale[x, y] = 255

    imgTk = ImageTk.PhotoImage(imgGrayscale)
    lbl.configure(image=imgTk)
    lbl.image = imgTk
    thresh.delete(0, END)




def opencv2Tkinter(img):
    # imgPill = Image.fromarray(img)
    # imgResized = imgPill.resize((670, 480), Image.ANTIALIAS)
    # imgTkinter = ImageTk.PhotoImage(imgResized)
    # lbl.configure(image=imgTkinter)
    # lbl.image = imgTkinter

    imgPill = Image.fromarray(img)
    imgTkinter = ImageTk.PhotoImage(imgPill)
    return imgTkinter


if __name__ == '__main__':
    root = Tk()

    frm = Frame(root, background='lightblue')
    frm.pack(side=BOTTOM, padx=15, pady=15)

    lbl = Label(root)
    lbl.pack()

    btn = Button(frm, text="Browser Image", command=browseImage)
    btn.pack(side=tk.LEFT)

    btnGray = Button(frm, text="Convert to Grayscale", command=rgb2Gray)
    btnGray.pack(side=tk.LEFT)

    btnExit = Button(frm, text="Exit", command=lambda: exit())
    btnExit.pack(side=tk.LEFT, padx=10)

    txtBinary = Label(frm, text="Threshold", font="Normal 12")
    txtBinary.pack(side=tk.LEFT)

    thresh = Entry(frm, font="Normal 12", bd=5)
    thresh.pack(side=tk.LEFT)
    
    btnBinary = Button(frm, text="Convert to Binary", command=rgb2Binary)
    btnBinary.pack(side=tk.LEFT)
    


    root.title("Image Browser App - 5200411488")
    root.geometry("1280x720")
    root.mainloop()

