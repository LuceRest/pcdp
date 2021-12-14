from tkinter import font
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from ttkbootstrap import Style
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


style = Style()
window = style.master


# Frame

frm = ttk.Frame(window, style='primary.TFrame')
# frm.pack(side='top')
frm.pack_propagate(0)
frm.pack(fill=tk.BOTH, expand=1)

frmTop = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
# frmTop.pack_propagate(0)
frmTop.grid(row=0, column=0, padx=20, pady=20)

frmImgOriginal = ttk.Frame(frmTop, style='info.TFrame', width=128, height=128)
frmImgOriginal.pack_propagate(0)
frmImgOriginal.pack(side="left", padx=20, pady=20)

frmBtnTop = ttk.Frame(frmTop, style='secondary.TFrame', width=100, height=200)
# frmBtnTop.pack_propagate(0)
frmBtnTop.pack(side="left", padx=20, pady=20)

frmImgFilter = ttk.Frame(frmTop, style='info.TFrame', width=128, height=128)
frmImgFilter.pack_propagate(0)
frmImgFilter.pack(side="left", padx=20, pady=20)


frmMid = ttk.Frame(frm, style='secondary.TFrame', width=500, height=550)
# frmMid.pack_propagate(0)
frmMid.grid(row=1, column=0, padx=10, pady=(10,20))

frmImgCanny = ttk.Frame(frmMid, style='info.TFrame', width=128, height=128)
# frmImgCanny.pack_propagate(0)
# frmImgCanny.pack(side="left", padx=10, pady=(20,2))
frmImgCanny.grid(row=0, column=0, padx=10, pady=(20,2))
frmImgCanny.grid_propagate(0)

frmImgSobel = ttk.Frame(frmMid, style='info.TFrame', width=128, height=128)
# frmImgSobel.pack_propagate(0)
# frmImgSobel.pack(side="left", padx=10, pady=(20,2))
frmImgSobel.grid(row=0, column=1, padx=10, pady=(20,2))
frmImgSobel.grid_propagate(0)

frmImgPrewitt = ttk.Frame(frmMid, style='info.TFrame', width=128, height=128)
# frmImgPrewitt.pack_propagate(0)
# frmImgPrewitt.pack(side="left", padx=10, pady=(20,2))
frmImgPrewitt.grid(row=0, column=2, padx=10, pady=(20,2))
frmImgPrewitt.grid_propagate(0)

frmBtnMid = ttk.Frame(frmMid, style='secondary.TFrame', width=848, height=43)
# frmBtnMid.pack_propagate(0)
# frmBtnMid.pack(side="bottom", padx=10, pady=30)
frmBtnMid.grid(row=1, column=0, columnspan=3, padx=10, pady=(3,20))
frmBtnMid.grid_propagate(0)


frmBottom = ttk.Frame(frm, style='secondary.TFrame', width=800, height=550)
# frmBottom.pack_propagate(0)
frmBottom.grid(row=2, column=0, padx=10, pady=(10,20))

frmImgErode = ttk.Frame(frmBottom, style='info.TFrame', width=128, height=128)
# frmImgErode.pack_propagate(0)
# frmImgErode.pack(side="left", padx=10, pady=(20,2))
frmImgErode.grid(row=0, column=0, padx=(175,0), pady=(20,2))
frmImgErode.grid_propagate(0)

frmImgClosing = ttk.Frame(frmBottom, style='info.TFrame', width=128, height=128)
# frmImgClosing.pack_propagate(0)
# frmImgClosing.pack(side="left", padx=10, pady=(20,2))
frmImgClosing.grid(row=0, column=1, padx=50, pady=(20,2))
frmImgClosing.grid_propagate(0)

frmBtnBottom = ttk.Frame(frmBottom, style='secondary.TFrame', width=848, height=43)
# frmBtnBottom.pack_propagate(0)
# frmBtnBottom.pack(side="bottom", padx=10, pady=30)
frmBtnBottom.grid(row=1, column=0, columnspan=3, padx=10, pady=(3,20))
frmBtnBottom.grid_propagate(0)


# Button

btnBrowse = ttk.Button(frmBtnTop, text='Browse Image', style='info.TButton', cursor="hand2", width=12)
# btnBrowse.grid(row=0, column=0, columnspan=0, padx=15)
btnBrowse.pack(side='top', pady=10)

btnFilter = ttk.Button(frmBtnTop, text='Filter', style='success.TButton', cursor="hand2", width=12)
# btnFilter.grid(row=2, column=0, padx=5, pady=10)
btnFilter.pack(side='top', pady=10)

btnExit = ttk.Button(frmBtnTop, text='Exit', style='danger.TButton', cursor="hand2", width=12)
# btnExit.grid(row=0, column=2, columnspan=2, padx=20)
btnExit.pack(side='top', pady=10)

btnCanny = ttk.Button(frmBtnMid, text='Canny', style='success.TButton', cursor="hand2", width=12)
btnCanny.grid(row=0, column=0, padx=80, pady=(10,0))
# btnCanny.pack(side='top', pady=(10,0))

btnSobel = ttk.Button(frmBtnMid, text='Sobel', style='success.TButton', cursor="hand2", width=12)
btnSobel.grid(row=0, column=1, padx=96, pady=(10,0))
# btnSobel.pack(side='top', pady=(10,0))

btnPrewitt = ttk.Button(frmBtnMid, text='Prewitt', style='success.TButton', cursor="hand2", width=12)
btnPrewitt.grid(row=0, column=2, padx=96, pady=(10,0))
# btnPrewitt.pack(side='top', pady=(10,0))

# St. El. Size

lblStElSize = ttk.Label(frmBtnBottom, text=f'St. El. Size : ', style='secondary.Inverse.TLabel')
lblStElSize.grid(row=0, column=0, padx=(30,0), pady=(10,0))

txtStElSize = ttk.Entry(frmBtnBottom, font="Normal 10",style='info.TEntry', width=7)
txtStElSize.grid(row=0, column=1, padx=(0,4), pady=(10,0))

btnErode = ttk.Button(frmBtnBottom, text='Erode', style='success.TButton', cursor="hand2", width=12)
btnErode.grid(row=0, column=2, padx=(50,0), pady=(10,0))
# btnErode.pack(side='top', pady=(10,0))

btnClosing = ttk.Button(frmBtnBottom, text='Closing', style='success.TButton', cursor="hand2", width=12)
btnClosing.grid(row=0, column=3, padx=(184), pady=(10,0))




# Label

lblImgOriginal = ttk.Label(frmImgOriginal)
# lblImgOriginal.grid(row=0, column=0)

lblResultFilter = ttk.Label(frmImgFilter)
# lblResultFilter.grid(row=0, column=0)

lblResultCanny = ttk.Label(frmImgCanny)
# lblResultCanny.grid(row=0, column=0)

lblResultSobel = ttk.Label(frmImgSobel)
# lblResultSobel.grid(row=0, column=0)

lblResultPrewitt = ttk.Label(frmImgPrewitt)
# lblResultPrewitt.grid(row=0, column=0)

lblResultErode = ttk.Label(frmImgErode)
# lblResultErode.grid(row=0, column=0)

lblResultClosing = ttk.Label(frmImgClosing)
# lblResultClosing.grid(row=0, column=0)


window.title("Image Filtering")
# window.geometry("1280x720")
# window.resizable(0, 0)
window.mainloop()


