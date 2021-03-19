# program_for_loop2
jumlah = int(input("Masukkan jumlah data"))

nama = []
umur = []

for i in range(0, jumlah):
    print(f"Data ke {i}")
    input_nama = input("Masukkan Nama:")
    input_umur = int(input("Masukkan umur: "))
    
    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"Mr {data_nama} berumur {data_umur} tahun")