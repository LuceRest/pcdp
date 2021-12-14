import cv2
import numpy as np

#baca image
citra = cv2.imread('lena.png')

#baca ukuran citra
jum_baris = len(citra[:])
jum_kolom = len(citra[0,:])

#tampilkan citra awal
cv2.imshow('citra awal', citra)

#inisialisasi faktor penskalaan
faktor_skala = 1.8      #faktor skala > 1: zoom in, faktor skala < 1: zoom out

#buat matrix zero untuk menampung gambar hasil translasi
jum_baris_baru = round(faktor_skala * jum_baris)
jum_kolom_baru = round(faktor_skala * jum_kolom)
citra_skala = np.zeros((jum_baris_baru, jum_kolom_baru, 3))      #angka 3 menyatakan 3 channel RGB

for brs_baru in range(jum_baris_baru):
    for klm_baru in range(jum_kolom_baru):
        #cek posisi brs dan klm pixel pada citra awal
        brs = int(brs_baru / faktor_skala)
        klm = int(klm_baru / faktor_skala)

        #isi pixel pada citra baru (citra skala)
        citra_skala[brs_baru, klm_baru] = citra[brs, klm]

#konversi citra_penskalaan menjadi uint8
citra_skala = citra_skala.astype(np.uint8)

#tampilkan citra hasil penskalaan
cv2.imshow("citra setelah penskalaan", citra_skala)

#tunggu hingga user menekan sembarang tombol
cv2.waitKey()