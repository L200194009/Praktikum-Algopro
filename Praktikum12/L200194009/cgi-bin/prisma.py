print("<!DOCTYPE html>\n")
print("""<html>
<head><title>Akses dengan SimpleHTTPRequestHadler</title></head>
<body><h3>Bangun Geometri</h3>""")
panjang = 10
lebar = 5
tinggi = 5
luas = panjang*lebar*tinggi
print ("""<table><tr><td>Nama Bangunan</td><td>:</td>Prisma Segiempat </td></tr>
                 <tr><td>Dimensi</td><td>:</td><td>3D</td></tr>
                 <tr><td>Rumus luas</td><td>:</td><td>panjang*lebar*tinggi</td></tr>""")
print("""<tr><td>Parameter 1</td><td>:</td><td>(0)</td></tr>""".format(panjang))
print("""<tr><td>Parameter 2</td><td>:</td><td>(0)</td></tr>""".format(lebar))
print("""<tr><td>Parameter 3</td><td>:</td><td>(0)</td></tr>""".format(tinggi))
print("""<tr><td>Luas</td><td>:</td><td>(0)</td></tr></table>""".format(luas))
print("""<script>var c = document.grtElementById("myCanvas")</script></body></html>"""))
