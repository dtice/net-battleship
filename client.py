import socket
import sys
import requests

port = int(sys.argv[2])
addr = '{}{}:{}'.format("http://",sys.argv[1],port)
x = sys.argv[3]
y = sys.argv[4]
print(addr)

fire = requests.post(addr, data={'x':x, 'y':y})

status = fire.status_code
response = fire.headers['hit']

print('HTTP{}; Hit={}'.format(status,response))
