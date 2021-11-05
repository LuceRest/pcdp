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

frmImgOri = ttk.Frame(frm, style='secondary.TFrame', width=900, height=500)
# frmImgOri.pack_propagate(0)
frmImgOri.grid(row=0, column=0, padx=25, pady=25)

frmImgOri1 = ttk.Frame(frmImgOri, style='info.TFrame', width=320, height=240)
frmImgOri1.pack_propagate(0)
frmImgOri1.pack(side="left", padx=20, pady=30)

frmBtn = ttk.Frame(frmImgOri, style='secondary.TFrame', width=100, height=200)
# frmBtn.pack_propagate(0)
frmBtn.pack(side="left", padx=20, pady=30)

frmImgOri2 = ttk.Frame(frmImgOri, style='info.TFrame', width=320, height=240)
frmImgOri2.pack_propagate(0)
frmImgOri2.pack(side="left", padx=20, pady=30)

# frmImgOri2 = ttk.Frame(frm, style='secondary.TFrame', width=600, height=512)
# frmImgOri2.pack_propagate(0)
# frmImgOri2.grid(row=0, column=2, padx=15, pady=15)


frmImgRes = ttk.Frame(frm, style='secondary.TFrame', width=320, height=240)
frmImgRes.pack_propagate(0)
frmImgRes.grid(row=1, column=0, padx=15, pady=30)



btnBrowse = ttk.Button(frmBtn, text='Browse Image', style='info.TButton', cursor="hand2", width=15)
# btnBrowse.grid(row=0, column=0, columnspan=0, padx=15)
btnBrowse.pack(side='top', pady=10)

btnAdd = ttk.Button(frmBtn, text='+', style='info.TButton', cursor="hand2", width=2)
# btnAdd.grid(row=2, column=0, padx=5, pady=10)
btnAdd.pack(side='top', pady=10)

btnsubtract = ttk.Button(frmBtn, text='-', style='info.TButton', cursor="hand2", width=2)
# btnsubtract.grid(row=1, column=0, padx=5, pady=10)
btnsubtract.pack(side='top', pady=10)

# valBright = ttk.Entry(frmBtn, style='info.TEntry', width=15)
# valBright.grid(row=1, column=1, columnspan=2, padx=5, pady=10)


btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2")
# btnExit.grid(row=0, column=2, columnspan=2, padx=20)
btnExit.pack(side='top', pady=10)

lblOriImg1 = ttk.Label(frmImgOri1)
# lblOriImg1.grid(row=0, column=0)

lblOriImg2 = ttk.Label(frmImgOri2)
# lblOriImg2.grid(row=0, column=0)

lblResultImg = ttk.Label(frmImgRes)
# lblResultImg.grid(row=0, column=0)

# sldBright = ttk.Scale(frmBtn, from_=-255, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=511)
# sldBright.grid(row=2, column=0, columnspan=4, padx=20, pady=10)


window.title("Adding or Subtracting Images  - 5200411488")
# window.geometry("1280x720")
# window.resizable(0, 0)
window.mainloop()


