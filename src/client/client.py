import select
import socket
import json
import sys

from client.actions.PostActions import PostActions
from enum import Enum
from common.model.Post import Post

class actionMenu(Enum):
        CREATE_POST = 1


class Client:

    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    def start(self):
        self._socket.connect((self.HOST, self.PORT))
        
        while True:
            inputStreams = [sys.stdin, self._socket]
            readStream, writeStream, errorStream = select.select(inputStreams,[],[])
            
            for stream in inputStreams: 
                if stream == self._socket: # if is receiving data from server
                    message = self._socket.recv(2048) 
                    print(message.decode('ascii')) 
                else: 
                    action = sys.stdin.readline()
                    match int(action):
                        case 1:
                            post = Post(None, "kevin", "pedro", 0, None, None, "darlan")
                            PostActions.sendPostRequest(post, self._socket)
                            
                    '''  '''
                            
                            
            ''' self._socket.send(json.dumps({"username": "ricardo"}).encode("ascii"))
            
            data = self._socket.recv(1024)
            
            print('Received from the server :',json.loads(data.decode("ascii")))
            
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                continue
            else:
                break '''
            
        self._socket.close()