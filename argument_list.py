#Belajar Argument List

# dengan 2 parameter
def jumlahkan(satu, dua):
    total = satu + dua
    print(f"Total {[satu, dua]} = {total}")

jumlahkan(10,10 )

# dengan 3 parameter
def jumlahkan(satu, dua, tiga):
    total = satu + dua + tiga
    print(f"Total {[satu, dua, tiga]} = {total}")

jumlahkan(10,10,10 )


# dengan 4 parameter
def jumlahkan(satu, dua, tiga=0, empat=0):
    total = satu + dua + tiga + empat
    print(f"Total {[satu, dua, tiga, empat]} = {total}")

jumlahkan(10,10 )


# dengan Argument List
# argument list cuman ada 1 dan di taruh paling belakang
def jumlahkan(*list_angka):
    total =0 
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10,10,10,10,10 )



