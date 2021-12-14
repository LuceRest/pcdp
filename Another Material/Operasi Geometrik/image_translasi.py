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
citra_translasi = np.zeros((jum_baris, jum_kolom, 3))       #angka 3 menyatakan 3 channel RGB

#lakukan translasi
geser_horizontal = -20        #negatif berarti ke kiri, positif berarti ke kanan
geser_vertikal = 35         #negatif berarti ke atas, positif berarti ke bawah

for brs in range(jum_baris):
    for klm in range(jum_kolom):
        #hitung posisi baris dan kolom yang baru
        brs_baru = brs + geser_vertikal
        klm_baru = klm + geser_horizontal

        #isi pixel pada citra_translasi dengan posisi baris dan kolom baru
        if (brs_baru < jum_baris and brs_baru >= 0):
            if (klm_baru < jum_kolom and klm_baru >= 0):
                citra_translasi[brs_baru, klm_baru] = citra[brs, klm]

#konversi citra_translasi menjadi uint8
citra_translasi = citra_translasi.astype(np.uint8)

#tampilkan citra hasil translasi
cv2.imshow("citra setelah translasi", citra_translasi)

#tunggu hingga user menekan sembarang tombol
cv2.waitKey()