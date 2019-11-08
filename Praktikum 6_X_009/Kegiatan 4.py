Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Nadia Zerlinda Taufik Putri"
>>> NIM = 1009
>>> Tinggi = 1.57
>>> Berat = 49
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Because the "Aku" data is written in perentheses
>>> Aku[0]
2001
>>> # Because the first object in "Aku" data is "TahunLahir", the value of "TahunLahir" is 2001
>>> a = NIM % 4; Aku[a]
49
>>> # Because the remaining result of 1009 devided by 4 is 1, so the result of Aku[1] is 49
>>> type(Aku[a])
<class 'int'>
>>> # Because the value of "Berat" is 1, 1 is an integer data type
>>> Aku[a:4]
(49, 1.57, 1009)
>>> # Because the object in "Aku" start from "Berat, Tinggi, NIM, Nama"
>>> type(Aku[4])
<class 'str'>
>>> # Because the "Aku[4]" data is string
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> # Because "Aku" data type is tuple, so can't changed with another data
>>> type(Data)
<class 'list'>
>>> # Because the "Data" data is written in brackets
>>> type(Data[4])
<class 'str'>
>>> # Because the value of "Data[4]" data is string
>>> Data[4][5]
' '
>>> # Because in value "Data[4]" object in the value start in 5, and this is "space"
>>> Data[4][a:6]
'adia '
>>> # Because in value "Data[4]" object inthe value start from "a" until "5" is "adia "
>>> Data[0] = "ok"; Data
['ok', 49, 1.57, 1009, 'Nadia Zerlinda Taufik Putri']
>>> # Because the first object has changed by "ok", and it call all list in "Data"
>>> Data[-1]
'Nadia Zerlinda Taufik Putri'
>>> # Because it is call from rear list
>>> range(1)
range(0, 1)
>>> # Because range of 1 is (0,1)
