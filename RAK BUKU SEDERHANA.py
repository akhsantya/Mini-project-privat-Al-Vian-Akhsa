buku = ["hujan",
        "hello cello",
        "dunia shopie"]

while True :
    print("-"*24)
    print(f"| {"no":^3}|{"judul":^16} |")
    print("-"*24)
    counter = 0
    while counter < len(buku):
        nomor = str(counter + 1)
        nama = buku[counter]
        print(f"| {nomor:^3}|{nama:^16} |")
        counter +=1
    print("-"*24)

    print("Mau Apa?")
    print("A. Tambah")
    print("B. Edit")
    print("C. Hapus")
    pilihan = input(">> ").upper()

    if pilihan == "A" :
        baru = input("tambahkan buku baru : ")
        buku.append(baru)
    elif pilihan == "B" :
        edit_no = int(input("masukkan nomor : "))
        edit_judul = input("masukkan judul : ")
        buku[edit_no - 1] = edit_judul 
    elif pilihan == "C" :
        hapus_no = int(input("masukkan nomor : "))
        buku.pop(hapus_no - 1)
    else :
        exit()

    