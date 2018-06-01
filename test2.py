import socket
import json
import time
import threading
from multiprocessing import Process



class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sv(self):

        # server_address = (self.host, self.port)
        self.sock.bind((self.host, self.port))

        # listen for incoming connections (server mode) with 5 connection at a time
        self.sock.listen(10)

        # while True:
        # wait for a connection
        print(self.port)
        print('waiting for a connection')

        connection, client_address = self.sock.accept()
        # receive the data in small chunks and print it
        while True:
            data = connection.recv(1024)
            if data:
                data1 = json.loads(data.decode('utf-8'))
                # output received data
                print("Data: %s" % data1)
                new_data = {"client": data1['client'], "time": time.strftime("_%S")}
                connection.sendall(json.dumps(new_data).encode('utf-8'))
            else:
                # no more data -- quit the loop
                print("no more data.")
                break

        # Clean up the connection
        # connection.shutdown()
        # connection.close()



class Clients:
    def __init__(self, host, port, client):
        self.host = host
        self.port = port
        self.client = client

    def cli(self):
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.host, self.port)
        sock.connect(server_address)
        # dumps json and send
        while True:
            new_data = {"client": self.client, "time": time.strftime("_%S")}
            sock.sendall(json.dumps(new_data).encode('utf-8'))
            # receive the data in small chunks and print it

            data = sock.recv(1024)
            if data:
                data1 = json.loads(data.decode('utf-8'))
                # output received data
                print("Data2: %s" % data1)
            time.sleep(1)


if __name__ == '__main__':
    host = 'localhost'
    port = 2012
    client = [1, 2, 3, 4, 5]

    for c in client:
        Process(name=c, target=Server(host, port).sv,).start()
        p = Process(target=Clients(host, port, c).cli, )
        p.start()
        p.join()






















