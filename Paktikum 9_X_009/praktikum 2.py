data = open("praktikum.txt" , "w")
data.write("Nadia Zerlinda \n")
data.write("L200194009 \n")
data.write("04/23/2001 \n")
data.close()

import shelve
S = open("praktikum.txt" , "r")
nama = S.readline()
tanggal = S.readline()
NIM = S.readline()
S.close()

print (nama)
print(tanggal)
print(NIM)
