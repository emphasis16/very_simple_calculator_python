def penjumlahan(x, y):
    z = x + y
    return z

def pengurangan(x, y):
    z = x - y
    return z


def perkalian(x, y):
    z = x * y
    return z

def pembagian(x, y):
    if y == 0:
        print("ERROR : Ga bisa dibagi 0 bro, belajar lagi \n")
        exit()
    z = x / y
    return z

def pembagianBulat(x, y):
    if y == 0:
        print("ERROR : Ga bisa dibagi 0 bro, belajar lagi \n")
        exit()
    z = x // y
    return z


print("""
Selamat Datang di Kalkulator Nono!!!
Tapi sayang banget cuma bisa tambah kurang kali bagi :(
Update incoming masbro \n
======================================================
""")

a = input("Masukkan bilangan pertama : ")
if not a.isnumeric():
    print("\nERROR : Masukan harus berupa angka. Program berhenti.\n")
    exit()

b = input("Masukkan bilangan kedua : ")
if not b.isnumeric():
    print("\nERROR : Masukan harus berupa angka. Program berhenti.\n")
    exit()

a = int(a)
b = int(b)

print("\n======================================================\n")
print(""""Silahkan Pilih operasi yang kamu mau, pilih dengan simbolnya :
1) Penjumlahan : +
2) Pengurangan : -
3) Perkalian : *
4) Pembagian dengan desimal : /
5) Pembagian tanpa desimal : //
""")

operator = input("Pilih: ")
print("\n======================================================\n")

hasil = None

if operator == "+":
    hasil = penjumlahan(a, b)
elif operator == "-":
    hasil = pengurangan(a, b)
elif operator == "*":
    hasil = perkalian(a, b)
elif operator == "/":
    hasil = pembagian(a, b)
elif operator == "//":
    hasil = pembagianBulat(a, b)
else :
    "ERROR : Itu operasi apa? Maaf tidak terdaftar\n"

if(hasil != None):
    print("Hasil: {}\n".format(hasil))
else:
    print("ERROR : Operasimu error hey, mungkin operator itu ga ada\n")