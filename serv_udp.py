from socket import *
from time import gmtime, strftime

HOST = gethostbyname(gethostname())
print(HOST)
PORT = 3000
BUFSIZE = 1024 #1 Kb
SOCKADDR = (HOST, PORT)
userServerSock = socket(AF_INET, SOCK_DGRAM) #Initialize socket with AF_INET: IP, SOCK_DGRAM: UDP
userServerSock.bind(SOCKADDR) #Connecting address

while True:
    print('\nWaiting...')
    data,addr = userServerSock.recvfrom(BUFSIZE) #Actual waiting cycle, reciving mess data & addr
    loc_data = data.decode('utf-8')
    #loc_data = data.decode('cp1251')
    print('Received from: ', addr, '\nData: ', loc_data, '\nTime: ', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    #answer = ('Answer to ' + addr[0] + ', echo: ' + data).encode('utf-8')
    #userServerSock.sendto(answer, addr)
userServerSock.close()