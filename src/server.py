import socket
import os

def tcp_server(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(2)
    print(f"TCP Server up at {host}:{port}")

#I need to make a function just to receive connections
#Do i need a thread running on this funct?
#How do i manage data then
def listener(s):
    while True:
        c, c_addr = s.accept()
        data = c.recv(1024)
        
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
        thread = treading.Thread(target=receive_data,args=(c,addr))

def receive_data(c,addr):
    while True:
        try:
            data = c.recv(1024).decode('utf-8')
            command, file = data.split(" ",1)

            if command == 'get':
                f_data = get(file)
                c.sendall(data.encode('utf-8'))
            elif command == 'put':#Needs implementation on client side
                put(file,f_data)
            elif command == 'cat':
                f_data = cat(file)
                c.sendall(data.encode('utf-8'))
            elif command == 'ls':
                f_data = ls()
                c.sendall(data.encode('utf-8'))
            else:
                print("Useful commands: [ get || put || cat || ls]")
            
        except:
            print("Error at receive_data")
            c.close()

    c.close()
