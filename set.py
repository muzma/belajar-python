# Belajar set
# untuk set diambil data unique, efeknya tidak dijamin urutan datanya indexnya /tidak mendukung index tapi menggunakan loop

# list => []
# tuple => ()
# set => {}

nama = {"Mustofa", "Mahmud", "Abubakar", "Mustofa"}

# untuk menambahkan data di Set menggunakan perintah add
nama.add("joko")
nama.add("dedi")
nama.add("dedi")
print(nama)

# untuk menghapus menggunakan perintah remove
nama.remove("Mustofa")

for data in nama:
    print(data)