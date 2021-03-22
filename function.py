# Belajar Module

def say_helo(nama):
    return f"Hello {nama}"

def total(*list_angka):
    hasil  = 0
    for data in list_angka:
        hasil = hasil + data
    return hasil