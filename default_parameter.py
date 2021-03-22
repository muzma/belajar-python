# Belajar Default Argument Value

# 1 parameter
def say_hello(name = "Mustofa"):
    print(f"Hello {name}")

say_hello("Mustofa")
say_hello()

# 2 parameter, Jika yang didepan menggunakan default value yang belakang juga harus menggunakan default value
def say_hello2(nama_depan="Mustofa", nama_belakang="Mahmud"):
    print(f"Hello {nama_depan} - {nama_belakang}")
say_hello2("muzma") # masuk ke parameter yang pertama
say_hello2(nama_belakang="abubakar")