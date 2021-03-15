from socket import *

#HOST = '192.168.56.1'
#HOST = '10.5.0.2'
HOST = '169.254.209.185'
#
#
#
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST, PORT)
userClientSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('Type your message: ')
    if not data: break
    data_b = data.encode('utf-8')
    userClientSock.sendto(data_b, SOCKADDR)
    #data, addr = userClientSock.recvfrom(BUFSIZE)
    #if not data: break
    print('Message sent succsessfully!')

userClientSock.close()