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
    lblImg.configure(image=imgTk)
    lblImg.image = imgTk


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
    lblImg.configure(image=imgTk)
    lblImg.image = imgTk


def rgb2BinaryBtn():
    global fln
    
    imgBinary = Image.open(fln).convert('L')
    pxBinary = imgBinary.load()

    horizontal = imgBinary.size[0]
    vertical = imgBinary.size[1]
    
    for x in range(horizontal):
        for y in range(vertical):
            if pxBinary[x, y] < int(thresh.get()):
                pxBinary[x, y] = 0
            else:
                pxBinary[x, y] = 255

    imgTk = ImageTk.PhotoImage(imgBinary)
    lblImg.configure(image=imgTk)
    lblImg.image = imgTk

    sliderBinary.set(thresh.get())
    thresh.delete(0, END)


def rgb2BinarySlider(e):
    global fln
    
    img = cv2.imread(fln, cv2.IMREAD_GRAYSCALE)
    thresh = int(sliderBinary.get())
    ret, imgBinary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    imgTk = opencv2Tkinter(imgBinary)
    lblImg.configure(image=imgTk)
    lblImg.image = imgTk



def opencv2Tkinter(img):
    imgPill = Image.fromarray(img)
    imgTkinter = ImageTk.PhotoImage(imgPill)
    return imgTkinter


if __name__ == '__main__':
    root = Tk()

    frmBtn = Frame(root)
    frmBtn.pack(side=BOTTOM, padx=15, pady=15)

    lblImg = Label(root)
    lblImg.pack()

    btn = Button(frmBtn, text="Browser Image", background="lightblue",activebackground='#0275D8', padx=2, pady=2, font="Normal 10", command=browseImage)
    btn.grid(row=0, column=0)

    btnGray = Button(frmBtn, text="Convert to Grayscale", background="lightblue",activebackground='#0275D8', padx=2, pady=2, font="Normal 10", command=rgb2Gray)
    btnGray.grid(row=0, column=1)

    btnExit = Button(frmBtn, text="Exit", background="#D9534F",activebackground='red', padx=2, pady=2, font="Normal 10", command=lambda: exit())
    btnExit.grid(row=0, column=2)

    txtBinary = Label(frmBtn, text="Threshold", font="Normal 10")
    txtBinary.grid(row=1, column=0)

    thresh = Entry(frmBtn, font="Normal 10", bd=3)
    thresh.grid(row=1, column=1)
    
    btnBinary = Button(frmBtn, text="Convert to Binary", background="lightblue",activebackground='#0275D8', padx=2, pady=2, font="Normal 10", command=rgb2BinaryBtn)
    btnBinary.grid(row=1, column=2)
    
    sliderBinary = Scale(frmBtn, from_=0, to=255, orient=HORIZONTAL, length=255, cursor="hand2", repeatdelay=5000, command=rgb2BinarySlider)
    sliderBinary.grid(row=2, column=0, columnspan=5)
    


    root.title("Image Browser App - 5200411488")
    root.geometry("1280x720")
    root.mainloop()

