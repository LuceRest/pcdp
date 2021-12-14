import cv2
import numpy as np

#baca image
citra = cv2.imread('lena.png')

#baca ukuran citra
jum_baris = len(citra[:])
jum_kolom = len(citra[0,:])

#tampilkan citra awal
cv2.imshow('citra awal', citra)

#buat matrix zero untuk menampung gambar hasil translasi
citra_rotasi = np.zeros((jum_baris, jum_kolom, 3))      #angka 3 menyatakan 3 channel RGB

#lakukan rotasi
sudut_rotasi = 25      

#konversi sudut_rotasi menjadi radian
sudut_radian = 3.14 * sudut_rotasi / 180

for brs in range(jum_baris):
    for klm in range(jum_kolom):
        #hitung posisi baris dan kolom yang baru
        brs_baru = round(brs * np.cos(sudut_radian) - klm * np.sin(sudut_radian))
        klm_baru = round(brs * np.sin(sudut_radian) + klm * np.cos(sudut_radian))

        #isi pixel pada citra_rotasi dengan posisi baris dan kolom baru
        if (brs_baru < jum_baris and brs_baru >= 0):
            if (klm_baru < jum_kolom and klm_baru >= 0):
                citra_rotasi[brs_baru, klm_baru] = citra[brs, klm]

#konversi citra_rotasi menjadi uint8
citra_rotasi = citra_rotasi.astype(np.uint8)

#tampilkan citra hasil rotasi
cv2.imshow("citra setelah rotasi", citra_rotasi)

#tunggu hingga user menekan sembarang tombol
cv2.waitKey()