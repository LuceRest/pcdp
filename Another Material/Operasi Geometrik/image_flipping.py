import cv2
import numpy as np

#baca image
citra = cv2.imread('lena.png')

#baca ukuran citra
jum_baris = len(citra[:])
jum_kolom = len(citra[0,:])

#tampilkan citra awal
cv2.imshow('citra awal', citra)

#buat matrix zero untuk menampung gambar hasil flipping
citra_flipping = np.zeros((jum_baris, jum_kolom, 3))        #angka 3 menyatakan 3 channel RGB

#lakukan flipping
flip_horizontal = 1     #jika 1: lakukan flip horizontal, jika 0: tidak melakukan apa2
flip_vertikal = 0       #jika 1: lakukan flip vertikal, jika 0: tidak melakukan apa2

for brs in range(jum_baris):
    for klm in range(jum_kolom):
        #hitung posisi kolom yang baru jika flip_horizontal = 1
        if (flip_horizontal == 1):
            klm_baru = (jum_kolom - 1) - klm
        else:
            klm_baru = klm
        
        #hitung posisi baris yang baru jika flip_vertikal = 1
        if (flip_vertikal == 1):
            brs_baru = (jum_baris - 1) - brs
        else:
            brs_baru = brs

        #isi pixel pada citra_flipping dengan posisi baris dan kolom baru
        citra_flipping[brs_baru, klm_baru] = citra[brs, klm]

#konversi citra_flipping menjadi uint8
citra_flipping = citra_flipping.astype(np.uint8)

#tampilkan citra hasil flipping
cv2.imshow("citra setelah pencerminan", citra_flipping)

#tunggu hingga user menekan sembarang tombol
cv2.waitKey()