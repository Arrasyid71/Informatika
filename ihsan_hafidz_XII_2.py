def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Tidak bisa menghitung modulus dengan nol!"
    return x % y

# bembuka1
print("Selamat datang di Kalkulator Sederhana!")
print("Saya di sini untuk membantu Anda melakukan perhitungan.")

# pembuka2
name = input("Boleh tahu siapa nama Anda? ")
print(f"Senang bertemu dengan Anda, {name}!")

print("\nPilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus (Sisa Hasil Pembagian)")

# memilih operasi
choice = input("Masukkan pilihan (1/2/3/4/5): ")

# memasukkan angka
angka1 = float(input(f"Baiklah {name}, sekarang masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Melakukan operasi
if choice == '1':
    print(f"Hasil: {angka1} + {angka2} = {add(angka1, angka2)}")
elif choice == '2':
    print(f"Hasil: {angka1} - {angka2} = {subtract(angka1, angka2)}")
elif choice == '3':
    print(f"Hasil: {angka1} * {angka2} = {multiply(angka1, angka2)}")
elif choice == '4':
    print(f"Hasil: {angka1} / {angka2} = {divide(angka1, angka2)}")
elif choice == '5':
    print(f"Hasil: {angka1} % {angka2} = {modulus(angka1, angka2)}")
else:
    print("Pilihan tidak valid!")

# Penutupan
print(f"Terima kasih sudah menggunakan kalkulator ini, {name}. Semoga harimu menyenangkan!")
