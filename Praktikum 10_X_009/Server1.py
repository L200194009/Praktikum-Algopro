#server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ' '
kamus = {'nama' : 'Nadia Zerlinda',
         'NIM' : 'L200194009',
         'angkatan' : '2019/2020',
         'keluar' : 'siapp!!'}
while data.lower() != 'quit':
    komm, addr = s.accept()
    while data.lower() != 'quit':
        data = komm.recv(1024)
        if data.lower() == 'quit':
            s.close()
            break
        print 'Pertanyaan : ',data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, erintah tidak dimengerti')
