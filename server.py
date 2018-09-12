# Simple WebServer Relative to Current Directory
# from http.server import *
# from socketserver import *
#
#
# def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
#     server_address = ('', 8000)
#     httpd = server_class(server_address, handler_class)
#     print("Running " + str(httpd.server_name) + " on " + str(httpd.server_port) + "...")
#     httpd.serve_forever()
# run()

import socket
import threading

bind_addr = '127.0.0.1'
bind_port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_addr, bind_port))
server.listen(1)

print("Listening on ", bind_addr, " : ", bind_port)

def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    x, y = str(request).split(';')
    client_socket.send('{}*{}={}'.format(x, y, int(x)*int(y))
    client_socket.close()

while True:
    client_sock, address = server.accept()
    print("Accepted connection from ", address[0], ":", address[1])
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
    )
    client_handler.start()
