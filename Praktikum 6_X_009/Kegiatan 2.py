import random
angka = random.randint(0,1000)

Nama = "Nadia Zerlinda Taufik Putri"
TanggalLahir = "23 April 2001"
NamaSingkat = Nama[0:15] + Nama[15] + "." + Nama[22] + "."
Ussername = Nama[0] + TanggalLahir[0] + TanggalLahir[9:13]
Password = Nama[0:4] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Ussername)
print(Password)
