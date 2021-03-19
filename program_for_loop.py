# Membuat program menggunakan for-loop, list dan range

banyak = int(input("Berapa banyak data?"))

nama = []
umur = []

for i in range(0,banyak):
    print(f"data ke {i}")
    input_nama = input("Nama : ")
    input_umur = int(input(" Umur: "))

    nama.append(input_nama)
    umur.append(input_umur)
    
print(nama)
print(umur)

for i in range(0, len(nama)):
    data_nama  = nama[i]
    data_umur = umur[i]
    print(f"Mr {data_nama} berumur {data_umur} tahun")