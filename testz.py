import socket
import json
import time
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def sv(self):

        # server_address = (self.host, self.port)
        self.sock.bind((self.host, self.port))

        # listen for incoming connections (server mode) with 5 connection at a time
        self.sock.listen(10)

        while True:
            # wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            # receive the data in small chunks and print it
            # while True:
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
        connection.close()


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
            print("Data2: %s" % data1)

        # close connection
        sock.close()


if __name__ == '__main__':
    host = 'localhost'
    port = 2018

    def start_serv(h, p):
        serv = Server(h, p)
        serv.sv()

    def client(h1, p1, c):
        # send at 10 second 
        for i in range(10):
            cl = Client_s(h1, p1, c)
            cl.cli()
            # wait second
            time.sleep(1)


    sr = threading.Thread(target=start_serv, args=(host, port))
    sr.daemon = True
    cl1 = threading.Thread(target=client, args=(host, port, 1))
    cl2 = threading.Thread(target=client, args=(host, port, 2))
    cl3 = threading.Thread(target=client, args=(host, port, 3))
    cl4 = threading.Thread(target=client, args=(host, port, 4))
    cl5 = threading.Thread(target=client, args=(host, port, 5))
    sr.start()
    cl1.start()
    cl2.start()
    cl3.start()
    cl4.start()
    cl5.start()
    cl1.join()
    cl2.join()
    cl3.join()
    cl4.join()
    cl5.join()









