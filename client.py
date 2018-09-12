import socket
import sys

arg = sys.argv
port = 8000

target = '127.0.0.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target, port))

client.send('{};{}'.format(arg[1], arg[2]))

response = client.recv(4096)

print response
