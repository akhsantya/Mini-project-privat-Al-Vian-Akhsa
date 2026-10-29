#===KALKULATOR SEDERHANA===

while True :
#pilihan operasi
    print("a. Penjumlahan")
    print("b. Pengurangan")
    print("c. Perkalian")
    print("d. Pembagian")
    print("e. Modulus") 
    print("f. Perpangkatan")

#milih operasi
    operasi = input("pilih operasi: ")

#input angka
    input1 = float(input("masukan angka pertama: "))
    input2 = float(input("masukan angka kedua: "))

    if operasi == "a":
        hasil = input1 + input2
        print(f"hasil penjumlahan: {hasil}")
    elif operasi == "b":
        hasil = input1 - input2
        print(f"hasil pengurangan: {hasil}")
    elif operasi == "c":
        hasil = input1 * input2
        print(f"hasil perkalian: {hasil}")
    elif operasi == "d":
        hasil = input1 / input2
        print(f"hasil pembagian: {hasil}")
    elif operasi == "e":
        hasil = input1 % input2
        print(f"hasil modulus: {hasil}")
    elif operasi == "f":
        hasil = input1 ** input2
        print(f"hasil perpangkatan: {hasil}")
    else:
        print("tidak valid")

    print("Mau lagi ga?")
    print("Y")
    print("G")
    pilihan = input("").upper()
    if pilihan == "Y" :
        continue
    else :
        break
print("udah ya")




