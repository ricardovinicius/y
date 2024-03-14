import socket
import json

class Client:
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    def start(self):
        self._socket.connect((self.HOST, self.PORT))
        
        while True:
            message = input("What message do u wanna send? ")
            
            self._socket.send(json.dumps({"username": "ricardo"}).encode("ascii"))
            
            data = self._socket.recv(1024)
            
            print('Received from the server :',json.loads(data.decode("ascii")))
            
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break
            
        self._socket.close()