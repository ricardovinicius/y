import socket

from _thread import *
import threading

class Server:
    
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.threadLock = threading.Lock()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def start(self):
        self._socket.bind((self.HOST, self.PORT))
        print(f"Socket binded to port {self.PORT}")
        
        self._socket.listen(100)
        print(f"Socket is listening for 100 conn")
        
        while True:
            conn, addr = self._socket.accept()
            
            self.threadLock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            
            
            start_new_thread(self.clientThread, (conn,))
            
        self._socket.close()
            
    
    def clientThread(self, conn):
        while True:
            data = conn.recv(1024)
            
            if not data:
                print('Bye')
                
                self.threadLock.release()
                break
            
            data = data[::-1]
            
            conn.send(data)
        
        conn.close()
        
