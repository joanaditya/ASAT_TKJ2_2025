'remidi_joan_21'
bilangan = []
for i in range(5):
    angka = int(input(f"Masukkan bilangan ke-{i+1}: "))
    bilangan.append(angka)
jumlah_genap = 0
for angka in bilangan:
    if angka % 2 == 0:
        jumlah_genap += 1
print(f"\nBilangan yang dimasukkan: {bilangan}")
print(f"Jumlah bilangan genap: {jumlah_genap}")