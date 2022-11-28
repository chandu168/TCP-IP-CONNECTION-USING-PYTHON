import socket
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 6666
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.connect((ip,port))
    string=input("enter string")
    server.send(bytes(string,"utf-8"))
    string1=server.recv(1024)
    string1=string1.decode("utf-8")
    print(string1)
