#client
import socket
import platform

hostname = 'localhost'
pesan = ' '
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50005))
print "Program komunikasi tentang server"
while pesan.lower() != 'quit':
    pesan = raw_input('Command : ')
    s.send(pesan)
    if pesan.lower() != 'quit':
        response = s.recv(1024)
        print 'Response : ', response
s.close()
