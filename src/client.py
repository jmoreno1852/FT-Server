import socket
import threading

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1",4444))
def write(c):
    while True:
        data = input("FT-Server>")
        if data != "ls":
            try:
                command, file = data.split(" ",1)
            except:
                print("Format: [ get || put || cat ] file, or: ls")
        else:
            command = "ls"

        if command == "get":
            print("Sending get...")
            c.send(data.encode('utf-8'))
            f_data = c.recv(1024).decode('utf-8')
            with open(file, "w") as f:
                f.write(f_data)
                
        elif command == "put":
            print("Sending put...")
            c.send(data.encode('utf-8'))
            confirm_message = c.recv(1024).decode('utf-8')
            if confirm_message == "ready":

                with open(file, "r") as f:
                    f_data = f.read()
                c.send(f_data.encode('utf-8'))
        
        elif command == "cat":
            print("Sending cat")
            c.send(data.encode('utf-8'))
            print(c.recv(1024).decode('utf-8'))
        
        elif command == "ls":
            print("Sending ls...")
            c.send(data.encode('utf-8'))
            print(c.recv(1024).decode('utf-8'))
        
        else:
            c.send(data.encode('utf-8'))
            print(c.recv(1024).decode('utf-8'))

write(c)
