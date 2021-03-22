# Method/ Function, tempat menyimpan kode blok
# ketika mendifine method diletakkan diatas

nama = []

# pendekatan tradisional 
#nama.append("mustofa")
#print("==========")
#for data in nama:
#    print(data)

#nama.append("mahmud")
#print("===========")
#for data in nama:
#    print(data)

#nama.append("abubakar")
#print("===========")
#for data in nama:
#    print(data)

# Menggunakan method
def print_nama():
    print("==========")
    for data in nama:
        print(data)    

# Menambahkan data
nama.append("Mustofa")
# panggil method
print_nama()

nama.append("Mahmud")
# panggil method
print_nama()

nama.append("Abubakar")
# panggil method
print_nama()



