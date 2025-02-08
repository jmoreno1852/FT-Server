from src.server import *
import threading
def main():
    host = "127.0.0.1"
    port = 4444

    s = tcp_server(host,port)
    thread = threading.Thread(target=handle_client,args=(s,))
    thread.start()

if __name__ == "__main__":
    main()
