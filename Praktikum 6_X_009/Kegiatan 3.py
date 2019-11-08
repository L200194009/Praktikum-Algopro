Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Nadia Zerlinda Taufik Putri"
>>> NIM = "L200194009"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Because the "X" data had changed to integer data type
>>> type(b)
<class 'int'>
>>> # Because the "Nama" data has a "len" intruction
>>> a / b
37.370370370370374
>>> # Because the result of 1009 devided by 27 is 37.370370370370374
>>> a // b
37
>>> # Because the meaning of "//" is divison with rounding down
>>> 10 * (a - 999)
100
>>> # Because the value of "a" minus 999 is 10, after that it will multipled
>>> b ** 2
729
>>> # Because the value of "b" square is 729
>>> a % b
10
>>> # Because the meaning of "%" is the remainder  of the division result
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Because the "c" data is a float
>>> a / c
80.72
>>> # Because the result of 1009 devided by 12.5 is 80.72
>>> a // c
80.0
>>> # Because the meaning of "//" is devision with rounding down
>>> a % c
9.0
>>> # Because the meaning of "%" is the reminder of the division result
>>> c > b
False
>>> # Because the value of "c" < value of "b"
>>> type(c > b)
<class 'bool'>
>>> # Because the "c > b" data had changed to boolean data type
>>> a > b and b > c
True
>>> # Because "a > b" is True and "b > c" is True
>>> a > 1100 or b < 10
False
>>> # Because "a > 1100" is False or "b < 10" is False
