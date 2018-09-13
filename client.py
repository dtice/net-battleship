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
headers = fire.headers
hit = headers['hit']

if 'sunk' in headers:
    sunk = headers['sunk']
    print('HTTP{}; Hit={}; Sunk={}'.format(status,hit,sunk))
else:
    print('HTTP{}; Hit={}'.format(status,hit))
