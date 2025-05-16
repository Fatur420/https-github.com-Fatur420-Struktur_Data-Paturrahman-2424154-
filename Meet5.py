# membuat program kalkulator sederhana
print("=== Kalkulator Sederhana ===")
print("Masukkan dua angka dan pilih operasi (+ : * - /)")

operasi = input("Masukkan operasi (+ - * /): ")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if operasi == "+":
    final = angka1 + angka2
    print("Hasil:", final)
elif operasi == "-":
    final = angka1 - angka2
    print("Hasil:", final)
elif operasi == "*":
    final = angka1 * angka2
    print("Hasil:", final)
elif operasi == "/":
    if angka2 != 0:
        final = angka1 / angka2
        print("Hasil:", final)
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Operasi tidak dikenali.")
