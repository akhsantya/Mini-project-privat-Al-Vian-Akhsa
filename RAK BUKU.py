buku = []

with open("FileMiniProject09.csv", "a", encoding="utf-8") as f :
    pass
with open("FileMiniProject09.csv", "r", encoding="utf-8") as f :
    for i in f :
        i = list(i.strip().split(","))
        i[2] = int(i[2])
        buku.append(i)

 
def tabel() :
    global buku
    print("-"*75)
    print(f"| {"No.":<3} | {"Judul":^35} | {"Tema":^15} | {"Halaman":<9} |")
    print("-"*75)
    for i in range(len(buku)) :
        print(f"| {i+1:<3} | {buku[i][0]:<35} | {buku[i][1]:<15} | {buku[i][2]:<9} |")
    print("-"*75)

def tambah() :
    global buku
    nama = input("masukkan nama : ")
    tema = input("masukkan tema : ")
    halaman = int(input("masukkan jumlah halaman : "))
    buku.append([nama, tema, halaman])

def kurang() :
    global buku 
    nomor = int(input("masukkan nomor : "))
    buku.pop(nomor-1)

def edit() :
    global buku
    nomor_edit = int(input("masukkan nomor : "))
    edit_nama = input("masukkan nama : ")
    edit_tema = input("masukkan tema : ")
    edit_halaman = int(input("masukkan jumlah halaman : "))
    baru = [edit_nama, edit_tema, edit_halaman]
    buku[nomor_edit - 1] = baru

while True :
    tabel()
    pilihan = input("masukkan pilihan : \nA. Tambah BUku\nB. Edit Buku\nC. Hapus Buku\nD. Keluar\n>>>").upper()
    if pilihan == "A" :
        tambah()
    elif pilihan == "B" :
        edit()
    elif pilihan == "C" :
        kurang()
    elif pilihan == "D" :
        with open("FileMiniProject09.csv", "w", encoding="utf-8") as f :
            pass


