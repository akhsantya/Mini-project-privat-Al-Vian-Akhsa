#===KALKULATOR LUAS===

#pilihan luas
print("pilih luas")
print("a. persegi")
print("b. persegi panjang")
print("c. segitiga")
print("d. lingkaran")
print("e. trapesium")

#input pilihan luas
pilihan = input("pilih luas: ")

#hitung luas
if pilihan == "a":
    panjang = float(input("masukan panjang: "))
    luas = panjang * panjang
    print(f"luas persegi: {luas}")
elif pilihan == "b":
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    luas = panjang * lebar
    print(f"luas persegi panjang: {luas}")
elif pilihan == "c":
    panjang = float(input("masukan panjang: "))
    tinggi = float(input("masukkan tinggi:"))
    luas = 0.5 * panjang * tinggi
    print(f"luas segitiga: {luas}")
elif pilihan == "d":
    jari_jari = float(input("masukan jari-jari: "))
    phi = 22/7 if jari_jari % 7 == 0 else 3.14
    luas = phi * jari_jari **2
    print(f"luas lingkaran: {luas}")
elif pilihan == "e":
    sisi1 = float(input("masukan sisi 1: "))
    sisi2 = float(input("masukan sisi 2: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 0.5 * (sisi1 + sisi2) * tinggi
    print(f"luas trapesium: {luas}")
else:
    print("tidak valid")

