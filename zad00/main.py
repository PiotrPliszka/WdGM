from PIL import Image
import numpy as np

obrazek = Image.open("PP.bmp")  # wczytywanie obrazu
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

tablica = np.asarray(obrazek)
print("typ danych tablicy:", tablica.dtype)
print(tablica.size)
print(tablica.shape)
ob_d = Image.fromarray(tablica)
ob_d.show()
print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)
dane_obrazka1 = tablica.astype(np.uint8)
print(dane_obrazka1)
print("piksel (50,30): ", tablica[30, 50])
print("piksel (90,40): ", tablica[40, 90])
print("piksel (99,0): ", tablica[0, 99])

# zapis tablicy do pliku
t1_text = open('t1.txt', 'w')
for rows in dane_obrazka1:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')

t1_text.close()

t2 = np.loadtxt("t1.txt", dtype=np.bool_)
dane_obrazka2 = Image.fromarray(t2)
dane_obrazka2.show()
t3 = np.loadtxt("t1.txt", dtype=np.uint8)
dane_obrazka3 = Image.fromarray(t3)
dane_obrazka3.show()
