import socket
import threading

Ip = "0.0.0.0"
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((Ip,PORT))
    server.listen(5)
    print(f"[*] Listening {Ip} : {PORT}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from{address[0]}:{address[1]}")
        client_handler = threading.Thread(target = handleclient(), args=(client,))
        client_handler.start()

def handleclient(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Receaved: {request.decode("utf-8")}")
        sock.send(b"ack")

if __name__=="__main__":
    main()
