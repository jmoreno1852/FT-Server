import socket
import os

def tcp_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(2)
    print(f"TCP Server up at {host}:{port}")
    while True:
        c, c_addr = s.accept()
        data = c.recv(1024)

#I need to make a function just to receive connections
#

def ls():
    return(os.listdir(path='.'))

def cat(file):
    try:
        with open(file , encoding="utf-8") as f:
            read_data = f.read()
        return read_data
    except OSError:
        print("Error while openning file")
def get():
    pass

def put():
    pass
