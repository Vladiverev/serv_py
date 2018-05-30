import socket
import json
import time


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def sv(self):
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (self.ip, self.port)
        sock.bind(server_address)

        # listen for incoming connections (server mode) with 5 connection at a time
        sock.listen(5)

        while True:
            # wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()

            try:
                # show who connected to us
                print('connection from', client_address)

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
            except Exception as e:
                print(e)
            else:
                # Clean up the connection
                connection.close()


if __name__ == '__main__':
    serv = Server('localhost', 2019)
    serv.sv()