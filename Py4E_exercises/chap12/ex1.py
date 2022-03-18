import socket
import re

inp = input('Enter webpage - ')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = re.split('/+', inp)
host = address[1]
print(host)
mysock.connect((host,80))

cmd1 = 'GET %s HTTP/1.0\r\n\r\n' % (inp)
cmd = cmd1.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
