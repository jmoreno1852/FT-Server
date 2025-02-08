import socket
import os
import threading
import sys
def tcp_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(2)
    print(f"TCP Server up at {host}:{port}")
    return s

def ls():
    return(os.listdir(path='.'))

def cat(file):
    try:
        with open(file , encoding="utf-8") as f:
            read_data = f.read()
        return read_data
    except OSError:
        print("Error while openning file")
def get(file):
    with open(file,"r") as f:
        return f.read()

def put(file, f_data): #Should this be on client??
    with open(file,"w") as f:
        f.write(f_data)

def handle_client(s):
    while True:
        c, addr = s.accept()
        print(f"Connection from {addr}")
        thread = threading.Thread(target=receive_data,args=(c,))
        thread.start()

def receive_data(c):
    while True:
        try:
            data = c.recv(1024).decode('utf-8')
            if data != "ls":
                try:
                    command, file = data.split(" ",1)
                except Exception as e:
                    print(e)

            if command == 'get':
                f_data = get(file)
                c.sendall(data.encode('utf-8'))
            elif command == 'put':#Needs implementation on client side
                c.send("ready".encode('utf-8'))
                f_data = c.recv(1024).decode('utf-8')
                put(file,f_data)
            elif command == 'cat':
                f_data = cat(file)
                c.sendall(f_data.encode('utf-8'))
            elif command == 'ls':
                f_data = ls()
                c.sendall(f_data.encode('utf-8'))
            else:
                data = "Useful commands: [ get || put || cat || ls]"
                c.send(data.encode('utf-8'))
        except Exception as e:
            print("e")
            c.close()
            sys.close()

    c.close()
