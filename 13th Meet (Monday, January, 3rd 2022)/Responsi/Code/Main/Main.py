from tkinter import font
import os
import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from ttkbootstrap import Style          # ttkbootstrap version 0.5.1
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# ----------| Function |----------

def setOriginal(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgOri.configure(image=imgTk)
    lblImgOri.image = imgTk
    lblImgOri.pack()

def setGray(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgGray.configure(image=imgTk)
    lblImgGray.image = imgTk
    lblImgGray.pack()

def setBiner(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgBiner.configure(image=imgTk)
    lblImgBiner.image = imgTk
    lblImgBiner.pack()

def setProcess1(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgProcess1.configure(image=imgTk)
    lblImgProcess1.image = imgTk
    lblImgProcess1.pack()

def setProcess2(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgProcess2.configure(image=imgTk)
    lblImgProcess2.image = imgTk
    lblImgProcess2.pack()

def setProcess3(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgProcess3.configure(image=imgTk)
    lblImgProcess3.image = imgTk
    lblImgProcess3.pack()

def setProcess4(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgProcess4.configure(image=imgTk)
    lblImgProcess4.image = imgTk
    lblImgProcess4.pack()

def setProcess5(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgProcess5.configure(image=imgTk)
    lblImgProcess5.image = imgTk
    lblImgProcess5.pack()

def setProcess6(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgProcess6.configure(image=imgTk)
    lblImgProcess6.image = imgTk
    lblImgProcess6.pack()

def setResult(img):
    imgTk = ImageTk.PhotoImage(img)
    lblImgResult.configure(image=imgTk)
    lblImgResult.image = imgTk
    lblImgResult.pack()    

def opencv2Pill(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgPill = Image.fromarray(img)
    return imgPill
    
def resizeImg(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur(img, k):
    return cv2.GaussianBlur(img, (k, k), 0)

def thresh(img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)

def erode(img, kernel):
    return cv2.erode(img, kernel, iterations=2)

def closing(img, kernel):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=6)
    
def dilate(img, kernel):
    return cv2.dilate(img, kernel, iterations=2)

def segementation(img):
    roi = img[0:697, 0:500]
    
    imgGray = grayscale(img)
    imgBlur = blur(imgGray, 15)
    imgThresh = thresh(imgBlur)

    # kernel = np.ones((3, 3), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

    # Morphology
    imgErode = erode(imgThresh, kernel)
    imgClosing = closing(imgErode, kernel)
    imgDilate = dilate(imgClosing, kernel)

    contImg = imgDilate.copy()
    contours, hierarchy = cv2.findContours(contImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw Contour
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area < 100:
            continue
        if len(cnt) < 0:
            continue

        ellipse = cv2.fitEllipse(cnt)
        x = int(ellipse[0][0])-20
        y = int(ellipse[0][1])+10
        if area >= 4500 and area <= 5000:       # Rp 100
            cv2.ellipse(roi, ellipse, (255,0,0), 2)
            cv2.putText(roi, '100', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
        elif area > 5000 and area < 5500:       # Rp 500 perunggu
            cv2.ellipse(roi, ellipse, (255,255,0), 2)
            cv2.putText(roi, '500', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
        elif area >= 5500 and area <= 6000:     # Rp 200
            cv2.ellipse(roi, ellipse, (255,0,255), 2)
            cv2.putText(roi, '200', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
        elif area > 6000 and area <= 7000:      # Rp 500 perak
            cv2.ellipse(roi, ellipse, (0,255,0), 2)
            cv2.putText(roi, '500', (x,y), cv2.FONT_HERSHEY_COMPLEX, .75, (0,255,0), 2)
        else:   
            cv2.ellipse(roi, ellipse, (0,0,255), 2)
   
    return imgGray, imgBlur, imgThresh, imgErode, imgClosing, imgDilate, roi
    

# ----------| Action |----------

def btnBrowseClicked():
    global fln

    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", 
                                    filetypes=(
                                        ("All Files", "*.*",),
                                        ("PNG File", "*.png"), 
                                        ("JPG File", "*.jpg"))
                                    )
    
    img = cv2.imread(fln)
    imgGray = grayscale(img)
    
    setOriginal(opencv2Pill(resizeImg(img, 125, 175)))
    setGray(opencv2Pill(resizeImg(imgGray, 125, 175)))

def btnThresholdClicked():
    global fln
        
    valueThresh = int(inputThresh.get())
    
    if valueThresh < 0 or valueThresh > 255:
        messagebox.showerror('Error', 'Input threshold value 0-255')
    else:
        img = cv2.imread(fln)
        ret, imgThresh = cv2.threshold(img, valueThresh, 255, cv2.THRESH_BINARY)
        setBiner(opencv2Pill(resizeImg(imgThresh, 125, 175)))

    inputThresh.delete(0, END)

def btnProccessClicked():
    global fln
    
    img = cv2.imread(fln)
    imgGray, imgBlur, imgThresh, imgErode, imgClosing, imgDilate, imgResult = segementation(img)

    setProcess1(opencv2Pill(resizeImg(imgGray, 125, 175)))
    setProcess2(opencv2Pill(resizeImg(imgBlur, 125, 175)))
    setProcess3(opencv2Pill(resizeImg(imgThresh, 125, 175)))
    setProcess4(opencv2Pill(resizeImg(imgErode, 125, 175)))
    setProcess5(opencv2Pill(resizeImg(imgClosing, 125, 175)))
    setProcess6(opencv2Pill(resizeImg(imgDilate, 125, 175)))
    setResult(opencv2Pill(resizeImg(imgResult, 250, 349)))
    

if __name__ == '__main__':
    fln = None
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
    lblOri = ttk.Label(frmRes, text=f'Citra Asli Fullcolor', style='secondary.Inverse.TLabel', justify='center')
    lblOri.grid(row=1, column=0, padx=20, pady=(5, 10))

    lblGray = ttk.Label(frmRes, text=f'Citra Grayscale', style='secondary.Inverse.TLabel', justify='center')
    lblGray.grid(row=1, column=1, padx=20, pady=(5, 10))

    lblBiner = ttk.Label(frmRes, text=f'Citra Biner', style='secondary.Inverse.TLabel', justify='center')
    lblBiner.grid(row=1, column=2, padx=20, pady=(5, 10))

    # Label Image
    lblImgOri = ttk.Label(frmImgOri)
    lblImgGray = ttk.Label(frmImgGray)
    lblImgBiner = ttk.Label(frmImgBiner)

    # Button
    frmBtnRes = ttk.Frame(frmRes, style='secondary.TFrame', width=625, height=75)
    frmBtnRes.grid(row=2, column=0, columnspan=4, padx=20, pady=10)

    btnBrowse = ttk.Button(frmBtnRes, text='Browse Image', style='success.TButton', cursor="hand2", width=12, command=btnBrowseClicked)
    btnBrowse.grid(row=0, column=0, columnspan=1, padx=(100,15), pady=10)

    btnThresh = ttk.Button(frmBtnRes, text='Threshold', style='success.TButton', cursor="hand2", width=12, command=btnThresholdClicked)
    btnThresh.grid(row=0, column=2, padx=(60,10), pady=10)

    valueDefault = tk.IntVar(value=200)
    inputThresh = ttk.Entry(frmBtnRes, font="Normal 10",style='info.TEntry', width=15, justify='center', textvariable=valueDefault)
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
    lblProcess1 = ttk.Label(frmProcess, text=f'Citra Hasil Grayscale\n(Operasi #1)', style='secondary.Inverse.TLabel', justify='center')
    lblProcess1.grid(row=1, column=0, padx=20, pady=(5, 20))

    lblProcess2 = ttk.Label(frmProcess, text=f'Citra Hasil Gaussian Blur\n(Operasi #2)', style='secondary.Inverse.TLabel', justify='center')
    lblProcess2.grid(row=1, column=1, padx=20, pady=(5, 20))

    lblProcess3 = ttk.Label(frmProcess, text=f'Citra Hasil Threshold\n(Operasi #3)', style='secondary.Inverse.TLabel', justify='center')
    lblProcess3.grid(row=1, column=2, padx=20, pady=(5, 20))

    lblProcess4 = ttk.Label(frmProcess, text=f'Citra Hasil Erosi\n(Operasi #4)', style='secondary.Inverse.TLabel', justify='center')
    lblProcess4.grid(row=1, column=3, padx=20, pady=(5, 20))

    lblProcess5 = ttk.Label(frmProcess, text=f'Citra Hasil Closing\n(Operasi #5)', style='secondary.Inverse.TLabel', justify='center')
    lblProcess5.grid(row=1, column=4, padx=20, pady=(5, 20))

    lblProcess6 = ttk.Label(frmProcess, text=f'Citra Hasil Dilasi\n(Operasi #6)', style='secondary.Inverse.TLabel', justify='center')
    lblProcess6.grid(row=1, column=5, padx=20, pady=(5, 20))

    # Label Image
    lblImgProcess1 = ttk.Label(frmImgProcess1)
    lblImgProcess2 = ttk.Label(frmImgProcess2)
    lblImgProcess3 = ttk.Label(frmImgProcess3)
    lblImgProcess4 = ttk.Label(frmImgProcess4)
    lblImgProcess5 = ttk.Label(frmImgProcess5)
    lblImgProcess6 = ttk.Label(frmImgProcess6)



    # ----------| Result |----------

    # Frame
    frmResult = ttk.Frame(frm, style='secondary.TFrame', width=900, height=550)
    frmResult.grid(row=0, column=1, rowspan=2, padx=30, pady=30)

    frmBtnResult = ttk.Frame(frmResult, style='secondary.TFrame', width=250, height=50)
    frmBtnResult.grid(row=0, column=0, padx=20, pady=(15,5))

    frmImgResult = ttk.Frame(frmResult, style='info.TFrame', width=250, height=349)
    frmImgResult.grid(row=1, column=0, padx=20, pady=(10,5))

    # Label
    lblResult = ttk.Label(frmResult, text=f'Citra Final Hasil Segmentasi', style='secondary.Inverse.TLabel', justify='center')
    lblResult.grid(row=2, column=0, padx=20, pady=(5,25))

    # Label Image
    lblImgResult = ttk.Label(frmImgResult)


    # Button
    btnProccess = ttk.Button(frmBtnResult, text='Proccess', style='success.TButton', cursor="hand2", width=12, command=btnProccessClicked)
    btnProccess.grid(row=0, column=0, padx=20, pady=(10,0))



    window.title("Responsi_PCD_Kel01_5200411488")
    # window.geometry("1280x720")
    window.resizable(0, 0)
    window.mainloop()

