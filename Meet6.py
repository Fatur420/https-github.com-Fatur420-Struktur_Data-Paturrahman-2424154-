# konditional statemen
# if else dalam satu line
# x if kondisi else yield


angka = 9

print ("positif" if angka > 0 else "negatife")
# ganjil / genap
print("Ganjil" if angka % 2 != 0 else "Genap")
# Program untuk mengecek apakah seseorang termasuk dewasa atau anak-anak

# Meminta input usia dari pengguna
umur = int(input("18: "))

# Mengecek dan menampilkan hasil berdasarkan umur
if umur >= 18:
    print("Anda termasuk DEWASA.")
else:
    print("Anda termasuk ANAK-ANAK.")
# Program untuk mengecek hak akses berdasarkan peran pengguna

# Meminta input dari pengguna
hak_akses = input("admin")

# Mengecek hak akses
if hak_akses.lower() == "admin":
    print("Anda memiliki FULL AKSES.")
else:
    print("AKSES DITOLAK (ACCESS DENIED).")

