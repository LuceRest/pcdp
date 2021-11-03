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

lblImgOri = ttk.Label(frmImgOri)
# lblImgOri.pack()

lblImgRes = ttk.Label(frmImgRes, style='info.TLabel')
# lblImgRes.grid(row=0, column=0)

btnBrowse = ttk.Button(frmBtn, text='Browse Image', style='info.TButton', cursor="hand2")
btnBrowse.grid(row=0, column=0, columnspan=2, padx=15)

btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2")
btnExit.grid(row=0, column=2, columnspan=2, padx=20)

valBright = ttk.Entry(frmBtn, style='info.TEntry')
valBright.grid(row=1, column=0, columnspan=2, padx=15, pady=10)

btnBright = ttk.Button(frmBtn, text='Brightening', style='info.TButton', cursor="hand2")
btnBright.grid(row=1, column=2, columnspan=2, padx=20, pady=10)

sldBright = ttk.Scale(frmBtn, from_=-255, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=511)
sldBright.grid(row=2, column=0, columnspan=4, padx=20, pady=10)


window.title("Image Browser App - 5200411488")
window.geometry("1280x720")
# window.resizable(0, 0)
window.mainloop()


