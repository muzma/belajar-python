# Belajar Method Return Value

#== Cara 1 ==
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
        print(f"Cara 1: Total {list_angka} = {total}")
        return total

total = jumlahkan(10,10,10,10)
# Mengambil data total?
print(total)

#== Cara 2 ==
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
        return (list_angka, total)        # data tuple

list_angka, total = jumlahkan(10,10,10,10)
# Mengambil data total?
print(f"Cara 2: Total {list_angka} ={total}")
print(f"Cara 2: Total {list_angka} ={total}")