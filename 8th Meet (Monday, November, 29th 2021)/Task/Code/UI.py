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


frm = ttk.Frame(window, style='primary.TFrame')
# frm.pack(side='top')
frm.pack_propagate(0)
frm.pack(fill=tk.BOTH, expand=1)

frmImg = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
# frmImg.pack_propagate(0)
frmImg.grid(row=0, column=0, padx=20, pady=20)

frmImgOri = ttk.Frame(frmImg, style='info.TFrame', width=512, height=512)
frmImgOri.pack_propagate(0)
frmImgOri.pack(side="left", padx=20, pady=30)

frmBtn = ttk.Frame(frmImg, style='secondary.TFrame', width=100, height=200)
# frmBtn.pack_propagate(0)
frmBtn.pack(side="left", padx=20, pady=30)

frmImgResult = ttk.Frame(frmImg, style='info.TFrame', width=512, height=512)
frmImgResult.pack_propagate(0)
frmImgResult.pack(side="left", padx=20, pady=20)


btnBrowse = ttk.Button(frmBtn, text='Browse Image', style='info.TButton', cursor="hand2", width=12)
# btnBrowse.grid(row=0, column=0, columnspan=0, padx=15)
btnBrowse.pack(side='top', pady=10)

btnFilter = ttk.Button(frmBtn, text='Filter', style='success.TButton', cursor="hand2", width=12)
# btnFilter.grid(row=2, column=0, padx=5, pady=10)
btnFilter.pack(side='top', pady=10)


btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2", width=12)
# btnExit.grid(row=0, column=2, columnspan=2, padx=20)
btnExit.pack(side='top', pady=10)

lblOriImg = ttk.Label(frmImgOri)
# lblOriImg.grid(row=0, column=0)

lblResultImg = ttk.Label(frmImgResult)
# lblResultImg.grid(row=0, column=0)

window.title("Image Filtering - 5200411488")
# window.geometry("1280x720")
# window.resizable(0, 0)
window.mainloop()


