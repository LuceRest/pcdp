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
faktor_skala = 0.5      #faktor skala > 1: zoom in, faktor skala < 1: zoom out

#buat matrix zero untuk menampung gambar hasil translasi
jum_baris_baru = round(faktor_skala * jum_baris)
jum_kolom_baru = round(faktor_skala * jum_kolom)
citra_skala = np.zeros((jum_baris_baru, jum_kolom_baru, 3))      #angka 3 menyatakan 3 channel RGB

print(jum_kolom_baru)
print(jum_baris_baru)

for brs in range(jum_baris):
    for klm in range(jum_kolom):
        #hitung baris baru dan kolom baru pada gamabr hasil penskalaan
        brs_baru = round(faktor_skala * brs)
        klm_baru = round(faktor_skala * klm)

        #isi pixel pada citra baru (citra skala)
        if (brs_baru < jum_baris_baru and klm_baru < jum_kolom_baru):
            citra_skala[brs_baru, klm_baru] = citra[brs, klm]

#konversi citra_penskalaan menjadi uint8
citra_skala = citra_skala.astype(np.uint8)

#tampilkan citra hasil penskalaan
cv2.imshow("citra setelah penskalaan", citra_skala)

#tunggu hingga user menekan sembarang tombol
cv2.waitKey()