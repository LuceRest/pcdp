from tkinter import font
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from ttkbootstrap import Style          # ttkbootstrap version 0.5.1
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk


# ----------| Function |----------

def setOriginal(img):
    imgTk = ImageTk.PhotoImage(img)
    # lblImgOriginal.configure(image=imgTk)
    # lblImgOriginal.image = imgTk
    # lblImgOriginal.pack()

def opencv2Pill(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgPill = Image.fromarray(img)
    return imgPill
    
def resizeImg(img, width, height):
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
    return img


# ----------| Action |----------

def btnBrowseClicked():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("All Files", "*.*",),
                                        ("PNG File", "*.png"), 
                                        ("JPG File", "*.jpg"))
                                    )
    
    img = opencv2Pill(resizeImg(cv2.imread(fln), 128, 128))
    setOriginal(img)


if __name__ == '__main__':
    style = Style()
    window = style.master


    # Frame Window

    frm = ttk.Frame(window, style='primary.TFrame')
    # frm.pack(side='top')
    frm.pack_propagate(0)
    frm.pack(fill=tk.BOTH, expand=1)


    # ----------| Resource |----------

    # Frame
    frmRes = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
    frmRes.grid(row=0, column=0, padx=30, pady=30)

    frmImgOri = ttk.Frame(frmRes, style='info.TFrame', width=125, height=175)
    frmImgOri.grid(row=0, column=0, padx=20, pady=20)

    frmImgGray = ttk.Frame(frmRes, style='info.TFrame', width=125, height=175)
    frmImgGray.grid(row=0, column=1, padx=20, pady=20)

    frmImgBiner = ttk.Frame(frmRes, style='info.TFrame', width=125, height=175)
    frmImgBiner.grid(row=0, column=2, padx=(20,20), pady=20)

    # frmImgBlank = ttk.Frame(frmRes, style='secondary.TFrame', width=125, height=175)
    # frmImgBlank.grid(row=0, column=3, padx=20, pady=20)

    # Label
    lblOri = ttk.Label(frmRes, text=f'Citra Asli Fullcolor', style='secondary.Inverse.TLabel')
    lblOri.grid(row=1, column=0, padx=20, pady=(5, 10))

    lblGray = ttk.Label(frmRes, text=f'Citra Grayscale', style='secondary.Inverse.TLabel')
    lblGray.grid(row=1, column=1, padx=20, pady=(5, 10))

    lblBiner = ttk.Label(frmRes, text=f'Citra Biner', style='secondary.Inverse.TLabel')
    lblBiner.grid(row=1, column=2, padx=20, pady=(5, 10))

    # Button
    frmBtnRes = ttk.Frame(frmRes, style='secondary.TFrame', width=625, height=75)
    frmBtnRes.grid(row=2, column=0, columnspan=4, padx=20, pady=10)

    btnBrowse = ttk.Button(frmBtnRes, text='Browse Image', style='success.TButton', cursor="hand2", width=12)
    btnBrowse.grid(row=0, column=0, columnspan=1, padx=(100,15), pady=10)

    btnThresh = ttk.Button(frmBtnRes, text='Threshold', style='success.TButton', cursor="hand2", width=12)
    btnThresh.grid(row=0, column=2, padx=(60,10), pady=10)

    inputThresh = ttk.Entry(frmBtnRes, font="Normal 10",style='info.TEntry', width=15)
    inputThresh.grid(row=0, column=3, padx=(10,30), pady=10)


    # ----------| Process |----------

    # Frame
    frmProcess = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
    # frmProcess.pack_propagate(0)
    frmProcess.grid(row=1, column=0, padx=30, pady=30)

    frmImgProcess1 = ttk.Frame(frmProcess, style='info.TFrame', width=125, height=175)
    frmImgProcess1.grid(row=0, column=0, padx=20, pady=(20,5))

    frmImgProcess2 = ttk.Frame(frmProcess, style='info.TFrame', width=125, height=175)
    frmImgProcess2.grid(row=0, column=1, padx=20, pady=(20,5))

    frmImgProcess3 = ttk.Frame(frmProcess, style='info.TFrame', width=125, height=175)
    frmImgProcess3.grid(row=0, column=2, padx=20, pady=(20,5))

    frmImgProcess4 = ttk.Frame(frmProcess, style='info.TFrame', width=125, height=175)
    frmImgProcess4.grid(row=0, column=3, padx=20, pady=(20,5))

    frmImgProcess5 = ttk.Frame(frmProcess, style='info.TFrame', width=125, height=175)
    frmImgProcess5.grid(row=0, column=4, padx=20, pady=(20,5))

    frmImgProcess6 = ttk.Frame(frmProcess, style='info.TFrame', width=125, height=175)
    frmImgProcess6.grid(row=0, column=5, padx=20, pady=(20,5))

    # Label
    lblProcess1 = ttk.Label(frmProcess, text=f'Citra Hasil \n(Operasi #1)', style='secondary.Inverse.TLabel')
    lblProcess1.grid(row=1, column=0, padx=20, pady=(5, 20))

    lblProcess2 = ttk.Label(frmProcess, text=f'Citra Hasil \n(Operasi #2)', style='secondary.Inverse.TLabel')
    lblProcess2.grid(row=1, column=1, padx=20, pady=(5, 20))

    lblProcess3 = ttk.Label(frmProcess, text=f'Citra Hasil \n(Operasi #3)', style='secondary.Inverse.TLabel')
    lblProcess3.grid(row=1, column=2, padx=20, pady=(5, 20))

    lblProcess4 = ttk.Label(frmProcess, text=f'Citra Hasil \n(Operasi #4)', style='secondary.Inverse.TLabel')
    lblProcess4.grid(row=1, column=3, padx=20, pady=(5, 20))

    lblProcess5 = ttk.Label(frmProcess, text=f'Citra Hasil \n(Operasi #5)', style='secondary.Inverse.TLabel')
    lblProcess5.grid(row=1, column=4, padx=20, pady=(5, 20))

    lblProcess6 = ttk.Label(frmProcess, text=f'Citra Hasil \n(Operasi #6)', style='secondary.Inverse.TLabel')
    lblProcess6.grid(row=1, column=5, padx=20, pady=(5, 20))


    # ----------| Result |----------

    # Frame
    frmResult = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
    frmResult.grid(row=0, column=1, rowspan=2, padx=30, pady=30)

    frmBtnResult = ttk.Frame(frmResult, style='secondary.TFrame', width=250, height=50)
    frmBtnResult.grid(row=0, column=0, padx=20, pady=(15,5))

    frmImgResult = ttk.Frame(frmResult, style='info.TFrame', width=250, height=349)
    frmImgResult.grid(row=1, column=0, padx=20, pady=(10,5))

    # Label
    lblResult = ttk.Label(frmResult, text=f'Citra Final Hasil Segmentasi', style='secondary.Inverse.TLabel')
    lblResult.grid(row=2, column=0, padx=20, pady=(5,25))

    # Button
    btnProccess = ttk.Button(frmBtnResult, text='Proccess', style='success.TButton', cursor="hand2", width=12)
    btnProccess.grid(row=0, column=0, padx=20, pady=(10,0))



    window.title("Responsi_PCD_Kel01_5200411488")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.mainloop()


