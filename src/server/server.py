import socket
import json
from common.model.Post import *

from _thread import *
import threading

class Server:
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.threadLock = threading.Lock()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def requestHandle(self, _socket):
        while True:
            try:
                mensagem = _socket.recv(1024).decode("utf-8")
                print("Mensagem recebida:", mensagem)
            except ConnectionAbortedError:
                print("Conexão encerrada pelo servidor.")
                break
        
        exit()
    # def responseSender(self, _socket):
        
    
    def start(self):
        self._socket.bind((self.HOST, self.PORT))
        print(f"Socket binded to port {self.PORT}")
        
        self._socket.listen(100)
        print(f"Socket is listening for 100 conn")
        
        self._initAllTables()
        
        while True:
            conn, addr = self._socket.accept()
            
            self.threadLock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            
            start_new_thread(self.clientThread, (conn,))
            
        self._socket.close()
            
    
    def clientThread(self, conn):
        requestHandleThread = threading.Thread(target=self.requestHandle, args=(conn, ))
        
        ''' data = json.loads(data.decode("ascii"))
            data["username"] = data["username"].upper()
            data = json.dumps(data) '''
            
        requestHandleThread.start()
        
        conn.close()
        
    def _initAllTables(self):
        Post._initTable()
        newPost = Post(None, "Guard", "Echo", 0, None, None, "Ricardo")
        print(newPost.__dict__)
        
