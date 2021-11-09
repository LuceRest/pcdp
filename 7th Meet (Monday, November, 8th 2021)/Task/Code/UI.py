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

frmImgOri = ttk.Frame(frm, style='secondary.TFrame', width=900, height=500)
# frmImgOri.pack_propagate(0)
frmImgOri.grid(row=0, column=0, padx=20, pady=(20,0))

frmImgOri1 = ttk.Frame(frmImgOri, style='info.TFrame', width=316, height=210)
frmImgOri1.pack_propagate(0)
frmImgOri1.pack(side="left", padx=20, pady=30)

frmBtn = ttk.Frame(frmImgOri, style='secondary.TFrame', width=100, height=200)
# frmBtn.pack_propagate(0)
frmBtn.pack(side="left", padx=20, pady=30)

frmImgOri2 = ttk.Frame(frmImgOri, style='info.TFrame', width=384, height=256)
frmImgOri2.pack_propagate(0)
frmImgOri2.pack(side="left", padx=20, pady=20)

frmSld = ttk.Frame(frm, style='secondary.TFrame', width=942, height=25)
frmSld.pack_propagate(0)
frmSld.grid(row=1, column=0, padx=20, pady=(0,10))
# frmSld.grid_propagate(0)

frmImgRes = ttk.Frame(frm, style='secondary.TFrame', width=576, height=384)
frmImgRes.pack_propagate(0)
frmImgRes.grid(row=2, column=0, padx=20, pady=20)

frmImgResult = ttk.Frame(frmImgRes, style='info.TFrame', width=576, height=384)
frmImgResult.pack_propagate(0)
frmImgResult.grid(row=0, column=0, padx=20, pady=20)



btnBrowse1 = ttk.Button(frmBtn, text='Browse Image 1', style='info.TButton', cursor="hand2", width=14)
# btnBrowse1.grid(row=0, column=0, columnspan=0, padx=15)
btnBrowse1.pack(side='top', pady=10)

btnBrowse2 = ttk.Button(frmBtn, text='Browse Image 2', style='info.TButton', cursor="hand2", width=14)
# btnBrowse2.grid(row=0, column=0, columnspan=0, padx=15)
btnBrowse2.pack(side='top', pady=10)

btnMerger = ttk.Button(frmBtn, text='→', style='success.TButton', cursor="hand2", width=2)
# btnMerger.grid(row=2, column=0, padx=5, pady=10)
btnMerger.pack(side='top', pady=10)


btnExit = ttk.Button(frmBtn, text='Exit', style='danger.TButton', cursor="hand2")
# btnExit.grid(row=0, column=2, columnspan=2, padx=20)
btnExit.pack(side='top', pady=10)

lblOriImg1 = ttk.Label(frmImgOri1)
# lblOriImg1.grid(row=0, column=0)

lblOriImg2 = ttk.Label(frmImgOri2)
# lblOriImg2.grid(row=0, column=0)

lblResultImg = ttk.Label(frmImgResult)
# lblResultImg.grid(row=0, column=0)
sldThresh = ttk.Scale(frmSld, from_=-255, to=255, value=0, orient='horizontal', style='info.Horizontal.TScale', length=511)

lblValue = ttk.Label(frmSld, text=f'Value of threshold : {sldThresh.get()}', style='info.Inverse.TLabel')
lblValue.pack(side='left', padx=50)

# sldThresh.grid(row=2, column=0, columnspan=4, padx=20, pady=10)
sldThresh.pack(side='left', padx=50, pady=0)

# current value label
# lblValue.grid(row=1, columnspan=2, sticky='n', ipadx=10, ipady=10)


window.title("Adding or Subtracting Images  - 5200411488")
# window.geometry("1280x720")
# window.resizable(0, 0)
window.mainloop()


