# Belajar Continue
# Kata kunci continue ini digunakan untuk menSkip process/data jika kondisi terpenuhi
for i in range(1, 100):
    # menskip yang genap
    if i % 2 == 0:
        continue
    print(i)