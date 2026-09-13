#pilihan satuan awal
print("PILIHAN SATUAN AWAL")
print("A. Celcius")
print("B. Reamur")
print("C. Fahrenheit")
print("D. Kelvin")

#pilih satuan awal
satuan_awal = input("PILIH SATUAN AWAL:")
match satuan_awal:
    case "A" | "B" | "C" | "D":
        pass 
    case _:
        print("TIDAK VALID")
        exit()
#brrti kalo milih satuan pake huruf kecil lgsg g valid

#nilai awal
nilai_awal = int(input("MASUKKAN NILAI AWAL:"))

#pilihan satuan akhir
print("PILIHAN SATUAN AKHIR")
print("A. Celcius")
print("B. Reamur")
print("C. Fahrenheit")
print("D. Kelvin")

#pilih satuan akhir
satuan_akhir = input("PILIH SATUAN AKHIR:")
match satuan_awal:
    case "A" | "B" | "C" | "D":
        pass  # valid, lanjut
    case _:
        print("TIDAK VALID")
        exit()

#konversi suhu
match (satuan_awal , satuan_akhir):
    case (X,Y) if X=="A" and Y=="A":
        nilai_akhir = nilai_awal
    case (X,Y) if X=="A" and Y=="B":
        nilai_akhir = nilai_awal * 4/5
    case (X,Y) if X=="A" and Y=="C":
        nilai_akhir = nilai_awal * 9/5 + 32
    case (X,Y) if X=="A" and Y=="D":
        nilai_akhir = nilai_awal + 273
    case (X,Y) if X=="B" and Y=="A":
        nilai_akhir = nilai_awal * 5/4
    case (X,Y) if X=="B" and Y=="B":
        nilai_akhir = nilai_awal 
    case (X,Y) if X=="B" and Y=="C":
        nilai_akhir = nilai_awal * 9/4 + 32
    case (X,Y) if X=="B" and Y=="D":
        nilai_akhir = nilai_awal * 5/4 + 273
    case (X,Y) if X=="C" and Y=="A":
        nilai_akhir = (nilai_awal - 32) * 5/9
    case (X,Y) if X=="C" and Y=="B":
        nilai_akhir = (nilai_awal - 32) * 4/9
    case (X,Y) if X=="C" and Y=="C":
        nilai_akhir = nilai_awal 
    case (X,Y) if X=="C" and Y=="D":
        nilai_akhir = (nilai_awal - 32) * 5/9 + 273
    case (X,Y) if X=="D" and Y=="A":
        nilai_akhir = nilai_awal - 273
    case (X,Y) if X=="D" and Y=="B":
        nilai_akhir = (nilai_awal - 273) * 4/5
    case (X,Y) if X=="D" and Y=="C":
        nilai_akhir = (nilai_awal - 273) * 9/5 + 32
    case (X,Y) if X=="D" and Y=="D":
        nilai_akhir = nilai_awal
    case _:
        print("TIDAK VALID")

#nilai akhir
print(f"NILAI AKHIR = {nilai_akhir}")




        
        
