import socket
import time
import json


class Client_s:
    def __init__(self, ip, port, client):
        self.ip = ip
        self.port = port
        self.client = client

    def cli(self):
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.ip, self.port)
        sock.connect(server_address)
        # dumps json and send
        new_data = {"client": self.client, "time": time.strftime("_%S")}
        sock.sendall(json.dumps(new_data).encode('utf-8'))
        # receive the data in small chunks and print it
        data = sock.recv(1024)
        if data:
            data1 = json.loads(data.decode('utf-8'))
            # output received data
            print("Data: %s" % data1)

        # close connection
        sock.close()


if __name__ == '__main__':
    c = [1, 2, 3, 4, 5]

    def client(clients):
        for i in clients:
            cl = Client_s('localhost', 2019, i)
            cl.cli()
            # wait second
            time.sleep(1)


    client(c)
    time.sleep(10)