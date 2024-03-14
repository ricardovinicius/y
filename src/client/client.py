import socket

class Client:
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def sendPost():
        self
    
    def start(self):
        self._socket.connect((self.HOST, self.PORT))
        
        while True:
            message = input("What message do u wanna send? ")
            
            self._socket.send(message.encode('ascii'))
            
            data = self._socket.recv(1024)
            
            print('Received from the server :',str(data.decode('ascii')))
            
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break
            
        self._socket.close()