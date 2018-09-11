import socket
import time
from contextlib import closing

class UDP_connection:
    host = None
    port = None
    bufsize = None
    client = None
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class UDP_Client(UDP_connection):
    def __init__(self):
        super(UDP_Client, self).__init__()
