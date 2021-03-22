# Progream management kontak
import function_app

#List of dictionary
daftar_kontak = []
# Data Dummy
#daftar_kontak.append({
#    "nama": "Mustofa",
#    "email": "mustofa_mahmud@yahoo.com",
#    "telepon":"08119110078"
#})

# Menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar program")

    menu = input("Pilih menu: ")

    if menu == "0":
        break
    elif menu == "1":
        function_app.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function_app.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function_app.hapus_kontak(daftar_kontak)
    elif menu =="4":
        function_app.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")

print("Program selesai berjalan, sampai jumpa")