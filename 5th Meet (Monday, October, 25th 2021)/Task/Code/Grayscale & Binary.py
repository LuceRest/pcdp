import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk
    

# fln = None

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

    print("\n\n{}\n\n".format(fln))
    
    img = mpimg.imread(fln)
    print("\n\n{}\n\n".format(img))
    plt.imshow(img)


    grayImage = np.zeros(img.shape)
    R = np.array(img[:, :, 0])
    G = np.array(img[:, :, 1])
    B = np.array(img[:, :, 2])

    R = (R * .299)
    G = (G * .587)
    B = (B * .114)

    Avg = (R+G+B)
    grayImage = img.copy()

    for i in range(3):
        grayImage[:,:,i] = Avg

    imgTk = ImageTk.PhotoImage(grayImage)
    lbl.configure(image=imgTk)
    lbl.image = imgTk
        

def rgb2Gray2():
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
    
    img = cv2.imread(fln)
    height, width, channels = img.shape

    imgBinary = np.zeros((height,width,1))
    imgGrayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = 120
    for i in np.arange(height):
        for j in np.arange(width):
            x = imgGrayscale.item(i,j)
            if x >= thresh:
                y = 1
            else :
                y = 0

            imgBinary.itemset((i,j,0),int(y))

    imgPill = Image.fromarray(imgBinary)
    imgTk = ImageTk.PhotoImage(imgPill)
    lbl.configure(image=imgTk)
    lbl.image = imgTk


def rgb2Binary2():
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

    imgBinary = np.zeros((img.size[0],img.size[1],1))

    thresh = 120
    for i in np.arange(img.size[0]):
        for j in np.arange(img.size[1]):
            x = img.getpixel((i,j))[0]
            if x >= thresh:
                y = 1
            else :
                y = 0

            imgBinary.itemset((i,j,0),int(y))
            # img.putpixel((x,y), (y, y, y))

    print(f'\n{imgBinary}\n-------------')

    imgNp = np.asarray(imgBinary)
    print(f'\n{imgNp}\n-------------')

    imgPill = Image.fromarray(imgNp, mode="L")
    print(f'\n{imgPill}\n-------------')

    imgTk = ImageTk.BitmapImage(imgPill)
    print(f'\n{imgTk}\n-------------')

    lbl.configure(image=imgTk)
    lbl.image = imgTk


def rgb2Binary3():
    global fln
    
    imgGrayscale = Image.open('mountain.jpg').convert('L')
    pxGrayscale = imgGrayscale.load()

    horizontal = imgGrayscale.size[0]
    vertical = imgGrayscale.size[1]

    thresh = 127
    
    for x in range(horizontal):
        for y in range(vertical):
            if pxGrayscale[x, y] < thresh:
                pxGrayscale[x, y] = 0
            else:
                pxGrayscale[x, y] = 255

    imgTk = ImageTk.PhotoImage(imgGrayscale)
    lbl.configure(image=imgTk)
    lbl.image = imgTk




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

    frm = Frame(root)
    frm.pack(side=BOTTOM, padx=15, pady=15)

    lbl = Label(root)
    lbl.pack()

    btn = Button(frm, text="Browser Image", command=browseImage)
    btn.pack(side=tk.LEFT)

    btnGray = Button(frm, text="Convert to Grayscale", command=rgb2Gray2)
    btnGray.pack(side=tk.LEFT)

    btnBinary = Button(frm, text="Convert to Binary", command=rgb2Binary3)
    btnBinary.pack(side=tk.LEFT)
    
    btnExit = Button(frm, text="Exit", command=lambda: exit())
    btnExit.pack(side=tk.LEFT, padx=10)


    root.title("Image Browser App - 5200411488")
    root.geometry("1280x720")
    root.mainloop()

