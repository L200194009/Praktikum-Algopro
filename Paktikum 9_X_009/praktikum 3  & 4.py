data = open("praktikum.txt" , "w")
data.write("Nadia Zerlinda \n")
data.write("L200194009 \n")
data.write("23/04/2001 \n")
data.close()

import shelve
A = shelve.open("praktikum.data")
A["Nama"] = ["Nadia Zerlinda"]
A["Tanggal"] = ["23/04/2001"]
A["NIM"] = ["L200194009"]
A.close()

A = shelve.open("praktikum.data")
print("Nama : ", A["Nama" [0:]])
print("Tanggal : ", A["Tanggal" [0:]])
print("NIM : ", A["NIM" [0:]])
A.close()
