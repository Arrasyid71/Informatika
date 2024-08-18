# Kalkulator Sederhana

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

# Sapaan
print("========================================")
print("  Selamat datang di Kalkulator Sederhana!")
print("========================================")
print("Saya di sini untuk membantu Anda melakukan perhitungan.\n")

# Meminta pengguna untuk memasukkan nama mereka
name = input("Boleh tahu siapa nama Anda? ")
print(f"\nSenang bertemu dengan Anda, {name}!\n")

print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus (Sisa Hasil Pembagian)")

# Meminta pengguna untuk memilih operasi
choice = input("\nMasukkan pilihan (1/2/3/4/5): ")

# Meminta pengguna untuk memasukkan dua angka
print(f"\nBaiklah {name}, sekarang masukkan angka yang ingin dihitung.")
num1 = float(input("Angka pertama: "))
num2 = float(input("Angka kedua: "))

# Melakukan operasi berdasarkan pilihan pengguna
print("\n========================================")
print("           Hasil Perhitungan")
print("========================================")

if choice == '1':
    print(f"Hasil: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Hasil: {num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"Hasil: {num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"Hasil: {num1} / {num2} = {divide(num1, num2)}")
elif choice == '5':
    print(f"Hasil: {num1} % {num2} = {modulus(num1, num2)}")
else:
    print("Pilihan tidak valid!")

# Penutupan
print("========================================")
print(f"Terima kasih sudah menggunakan kalkulator ini, {name}.")
print("Semoga harimu menyenangkan!")
print("========================================")
