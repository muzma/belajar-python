# Program Management Kontak
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("================")
        print(f"Nama: {kontak['nama']}")
        print(f"Email: {kontak['email']}")
        print(f"Telepon: {kontak['telepon']}")
    
def new_kontak():
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("No Telp yang akan dihapus:")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        print(daftar_kontak['telepon'])
        if telepon == daftar_kontak['telepon']:
            index = i
            break
    if index == -1:
        print("Data tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Berhenti berhasil menhapus data")

    del daftar_kontak[index]

def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Nama yang dicari: ")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.find(nama_yg_dicari) != -1:
        # untuk mengakali pencarian yang case sensitif bisa menggunakan function lowercase/dikecilkan semua
        #if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("================")
            print(f"Nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"Telepon: {kontak['telepon']}")