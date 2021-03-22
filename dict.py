# Belajar Tipe data Dictionary
# beda dictionary dengan yang lain (list, tuple, set)
# Data kumpulan 

customer = {"Name":"Mustofa" , "Age": 30, "Address":"Jombang"} # Key, Dictionary pakai key

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

# tambah data untuk Dictionary
customer["Company"] = "x"
customer["Name"] = " Mustofa Mahmud"

# menghapud data
del customer["Address"]

#cara 1
for key in customer:
    value = customer[key]
    print(f"{key} - {value}")
 
#cara 2
for key in customer.items():
    print(f"{key[0]} - {key[1]}")

# cara 3
for key, value in customer.items():
    print(f"{key} - {value}")

#items
print(customer.items())