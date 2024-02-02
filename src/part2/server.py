import sys
import socket
from threading import Thread

ipAddr = "127.0.0.1"
port = 4000

maxConnections = 5

def clientRequestHandler():
    # From part 1
    pass

def dispatcher():
    while True:
        connection, clientIpAddr = connectSocket.accept()

        t = Thread(target=clientRequestHandler, args=None)

        t.run()

if __name__ == '__main__':
    connectSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connectSocket.bind((ipAddr, port))

    connectSocket.listen(maxConnections)

    dispatcher()
