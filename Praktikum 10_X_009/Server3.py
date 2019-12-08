#server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50006))
s.listen(5)
print "Server penjawab otomatis sudah siap"
perintah = ' '
p=0
l=0
t=0
a=p*t
b=l*t

while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item[0]
        if perintah == 'keluar':
            komm.send('-')
            s.close()
            break
        print "pesan : ", perintah
        if len (item) ==2:
            if perintah == 'panjang':
                p=int(item[1])
                komm.send('panjang disimpan')
            elif perintah == 'tinggi':
                t=int(item[1])
                komm.send('tinggi disimpan')
            elif perintah == 'lebar':
                l=int(item[1])
                komm.send('lebar disimpan')
                
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung' :
            L = float(p*l + 2*a-b)
            response = 'Luas prisma dengan panjang {} lebar{} tinggi {} adalah{}'.format(p,l,t,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
        
