import socket
import time
from contextlib import closing


class UDP_connection:
    Configed = 0
    host = None
    port = None
    bufsize = None
    sock = None

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def Config(self, host='127.0.0.1', port='4000', bufsize='4096'):
        self.host = host
        self.port = port
        self.bufsize = bufsize
        self.Configed = 1
        pass

    def Send(self, messages):
        if self.Configed == 0:
            print("First config this connection.")
            pass
        count = 0
        with closing(self.sock):
            while True:
                message = messages.format(count).encode('utf-8')
                print(message)
                self.sock.sendto(message, (self.host, self.port))
                count += 1
                time.sleep(1)
        return

    def Recieve(self):
        if self.Configed == 0:
            print("First config this connection.")
            pass
        with closing(self.sock):
            self.sock.bind((self.host, self.port))
            retlist = []
            while True:
                retlist.append(self.sock.recv(self.bufsize))
        return retlist
