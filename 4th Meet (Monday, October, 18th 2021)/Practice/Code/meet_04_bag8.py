from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


def showImage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    print("Image path : ", fln)
    img = Image.open(fln)
    imgTk = ImageTk.PhotoImage(img)


    lbl.configure(image=imgTk)
    lbl.image = imgTk

root = Tk()

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browser Image", command=showImage)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=10)


root.title("Image Browser App")
root.geometry("500x400")
root.mainloop()




