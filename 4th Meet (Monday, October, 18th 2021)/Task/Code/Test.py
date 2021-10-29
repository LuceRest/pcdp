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
                                    filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    print("Image path : ", fln)
    img = Image.open(fln)
    imgTk = ImageTk.PhotoImage(img)


    lbl.configure(image=imgTk)
    lbl.image = imgTk

def showRed():
    global fln

    # img = Image.open(fln)
    # r,g,b = Image.Image.split(img)

    # print("r : ",r)
    # print("g : ",g)
    # print("b : ",b)

    # g = Image.Image.convert(g, "RGB", colors=0)
    # b = Image.Image.convert(b, "RGB", colors=0)
    # img = Image.merge('RGB', (r,g,b))
    

    # imgTk = ImageTk.PhotoImage(img)

    # lbl.configure(image=imgTk)
    # lbl.image = imgTk

    # ------------------------------------


    img = Image.open(fln)
    # r,g,b = Image.Image.split(img)
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            img.putpixel((x,y), (r, 0, 0))

    imgTk = ImageTk.PhotoImage(img)
    lbl.configure(image=imgTk)
    lbl.image = imgTk

    
    # ------------------------------------

    # img = Image.merge("RGB", (r,g,b))

    # img = cv.imread(fln)
    # b,g,r = cv.split(img)
    # black = np.zeros(img.shape[:2], img.dtype)
    # img = cv.merge([black,black,r])

    # imgTk = ImageTk.PhotoImage(img)

    # lbl.configure(image=imgTk)
    # lbl.image = imgTk

    # ------------------------------------





    
    # print(img)



root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browser Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Red", command=showRed)
btn2.pack(side=tk.LEFT, padx=10)

btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)


root.title("Image Browser App")
root.geometry("1280x720")
root.mainloop()




