import socket
import sys
import time

port = int(sys.argv[1]) if len(sys.argv) > 1 else 0

sock = socket.socket()
sock.bind(('localhost', port))
port = sock.getsockname()[1]

print(f"Server on port {port}")
sock.listen(1)
sock.settimeout(10)

try:
    client, addr = sock.accept()
    client.send(b"HTTP/1.1 200 OK\r\n\r\n<h1>Hello</h1>")
    client.close()
except:
    pass

sock.close()
print("\nServer dead")
