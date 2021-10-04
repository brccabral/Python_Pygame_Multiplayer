import socket

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.23"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
    
    def connect(self):
        try:
            self.client.connect(self.addr)
        except Exception as e:
            print(e)
            pass