'remidi_joan_21'
def luas_persegi(sisi):
    return sisi * sisi
def luas_lingkaran(r):
    return 3.14 * r * r
print("Menu Pilihan:")
print("1. Luas Persegi")
print("2. Luas Lingkaran")
pilihan = input("Pilih menu (1/2): ")
if pilihan == "1":
    sisi = float(input("Masukkan panjang sisi persegi: "))
    hasil = luas_persegi(sisi)
    print(f"Luas persegi dengan sisi {sisi} adalah {hasil}")
elif pilihan == "2":
    r = float(input("Masukkan jari-jari lingkaran: "))
    hasil = luas_lingkaran(r)
    print(f"Luas lingkaran dengan jari-jari {r} adalah {hasil}")
else:
    print("Pilihan tidak valid.")