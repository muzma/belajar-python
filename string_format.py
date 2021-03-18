# Belajar String Format
nama_depan = "Mustofa"
nama_tengah = "Mahmud"
nama_belakang = "Abubakar"

# versi classic
# nama_lengkap = "Assalamualaikum " + nama_depan +" "+ nama_tengah + " " + nama_belakang
# versi simple, untuk mengenali variable String di python jangan lupa gunakan "f" didepannya
nama_lengkap = f"Assalamualaikum {nama_depan} {nama_tengah} {nama_belakang}"

print(nama_lengkap)