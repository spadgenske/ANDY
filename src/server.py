#Cyclops server test
#By Tyler Spadgenske

import socket
from tts import say

class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.port = 5150
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print 'Listing for a client...'
        self.client, self.addr = self.server.accept()
        print 'Accepted connection from ', self.addr
        self.client.send(str.encode('Connection made with Andy'))

    def get_cmd(self):
        self.data = self.client.recv(1024)
        print 'Recieved data from client: ', bytes.decode(self.data)

        return self.data

    def end(self):
        print 'Closing connection...'
        self.client.send(str.encode('exit'))
        self.client.close()
        
def start():
    serv = Server()
    while True:
        files = open('/home/pi/ANDY/src/cmd.txt', 'w')
        cmd = serv.get_cmd()
        print type(cmd)
        files.write(cmd)
        files.close()
        while True:
            readit = open('/home/pi/ANDY/src/cmd.txt', 'r')
            lines = readit.readlines()
            if lines == []:
                break
        
    serv.end()
        

if __name__ == '__main__':
    start()
            
