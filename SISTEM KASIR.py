list_menu = [["Nasi goreng", 12000],
             ["Bakmi Gooreng", 14000],
             ["Kwetiaw Goreng", 14000],
             ["Capcay Goreng / Kuah", 15000],
             ["Es Teh / Panas", 3000],
             ["Es Teh Kampul / Panas", 4000]]

list_pesanan = []

    
lagi = True
while lagi:
    print("+-" + "-"*3 +"---" + "-"*25 + "-----" +"-"*8 + "-+")
    print("| No. | Menu                      | Harga      |")
    print("+-" + "-"*3 +"---" + "-"*25 + "-----" +"-"*8 + "-+")
    counter = 0
    while counter < len(list_menu):
        nomor = str(counter + 1)
        menu = list_menu[counter][0]
        harga = f"{list_menu[counter][1]:,}"
        print("| " + " "*(3-len(nomor)) + nomor + " | " + menu + " "*(25-len(menu)) + " | Rp" + " "*(8-len(harga)) + harga + " | ")
        counter +=1
    print("+-" + "-"*3 +"---" + "-"*25 + "-----" +"-"*8 + "-+")

    print("List Pesanan :") 
    if len(list_pesanan) == 0:
        print("1.")
    else:
        counter = 0
        while counter < len(list_pesanan):
            nama_menu = list_pesanan[counter][0]
            jumlah = list_pesanan[counter][1]
            nama = list_menu[nama_menu][0]
            print(f"{counter + 1}. {nama} x{jumlah}")
            counter += 1

    print("Mau Apa?")
    print("A. Tambah Pesanan")
    print("B. Edit Pesanan")
    print("C. Hapus Pesanan")
    print("D. Bayar Pesanan")
    print("E. Keluar")

    pesanan = input(">> ").upper()

    match pesanan:
        case "A":
            no_menu = int(input("Pilih no. menu : "))
            jumpes= int(input("Jumlah : "))
            if no_menu < 1 or no_menu > len(list_menu):
                print(">> GA VALID!!")
            else:
                list_pesanan.append([no_menu - 1, jumpes])
                print(">> Pesanan ditambahkan!")
        case "B" :
            no_edit = int(input("Masukkan Nomor Yang Akan Diedit : "))
            no_menu_baru = int(input("Pilih no. menu : "))
            jumpes_baru= int(input("Jumlah : "))
            list_pesanan[no_edit - 1] = no_menu_baru - 1, jumpes_baru
        case "C" :
            no_hapus = int(input("Masukkan Nomor  Pesanan Yang Akan Dihapus : "))
            list_pesanan.pop(no_hapus - 1)
        case "D" :
            total = sum(list_menu[p[0]][1] * p[1] for p in list_pesanan)
            print(f"Total Pembelian Sebesar Rp {total:,}")
        case "E":
            lagi = False
            print("tenkyuuuu yaaa")
            exit()
        case _:
            print("eror")
            




