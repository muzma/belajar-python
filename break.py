# Belajar Break
# Menghentikan proses

for i in range(1, 100):
    if i % 50 == 0:
        break
    print(i)

# Perulangan yang terus menerus (tidak berhenti)
# Beda dengan while loop yang membutuhkan sample data
while True:
    data = input("Data: ")
    if data == "x":
        break
    print(data)
