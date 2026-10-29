nilai_siswa = {"Andre" : 78, "Hena" : 90, "Tono" : 67}

while True :
    print("-"*18)
    print(f"|{"nama":^7}|{"nilai":^7} |")
    print("-"*18)
    for i in nilai_siswa :
        print(f"|{i:^7}|{nilai_siswa[i]:^7} |")
    print("-"*18)

    
    print("mau apa?")
    print("A. Tambah")
    print("B. Hapus")
    print("C. Edit")
    print("D. Keluar")
    pilihan = input(">> ").upper()  


    if pilihan == "A" :
        tambah_nama = input("masukkan nama  : ").capitalize()
        tambah_nilai = int(input("masukkan nilai : "))
        if tambah_nama not in nilai_siswa :
            nilai_siswa[tambah_nama] = tambah_nilai
        else :
            print("DATA SUDAH ADA")
    elif pilihan == "B" :
        key_hapus = input("masukkan nama : ").capitalize()
        if key_hapus in nilai_siswa :
            nilai_siswa.pop(key_hapus)
        else :
            print("DATA TIDAK DITEMUKAN")
    elif pilihan == "C" :
        edit_nama = input("masukkan nama  : ").capitalize()
        edit_nilai = int(input("masukkan nilai : "))
        if edit_nama in nilai_siswa :
            nilai_siswa[edit_nama] = edit_nilai
        else :
            print("DATA TIDAK DITEMUKAN")
    else :
        exit()