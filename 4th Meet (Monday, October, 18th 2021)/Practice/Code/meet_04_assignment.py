from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
import cv2 as cv


def showImage():
    global image

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                     filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"),
                                                ("All Files", "*.*")))
    print("Image path :", fln)

    # Read image -> save to global image variabel
    image = cv.imread(fln)

    img = Image.open(fln)
    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk


def imgRed():
    global image

    img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    img[:, :, 1] = 0
    img[:, :, 2] = 0

    imgTK = Image.fromarray(img)
    imgTK = ImageTk.PhotoImage(imgTK)
    lbl.configure(image=imgTK)
    lbl.image = imgTK


def imgGreen():
    global image

    img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    img[:, :, 0] = 0
    img[:, :, 2] = 0

    imgTK = Image.fromarray(img)
    imgTK = ImageTk.PhotoImage(imgTK)
    lbl.configure(image=imgTK)
    lbl.image = imgTK


def imgBlue():
    global image

    img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    img[:, :, 0] = 0
    img[:, :, 1] = 0

    imgTK = Image.fromarray(img)
    imgTK = ImageTk.PhotoImage(imgTK)
    lbl.configure(image=imgTK)
    lbl.image = imgTK


"""
PROGRAM START HERE
"""
root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

# Global variabel
image = []

btn1 = Button(frm, text="Browse Image", command=showImage)
btn1.pack(side=tk.LEFT, padx=10)

btn2 = Button(frm, text="Red", command=imgRed)
btn2.pack(side=tk.LEFT, padx=10)

btn3 = Button(frm, text="Green", command=imgGreen)
btn3.pack(side=tk.LEFT, padx=10)

btn4 = Button(frm, text="Blue", command=imgBlue)
btn4.pack(side=tk.LEFT, padx=10)

btn5 = Button(frm, text="Exit", command=lambda: exit())
btn5.pack(side=tk.LEFT, padx=10)

root.title("Image Broser App")
root.minsize(500, 400)
root.geometry("500x400")
root.mainloop()
