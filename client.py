import socket
import sys
import requests

# sets coordinates, port, and address according to arguments
port = int(sys.argv[2])
addr = '{}{}:{}'.format("http://",sys.argv[1],port)
x = sys.argv[3]
y = sys.argv[4]

# attempts post request at given address with given payload
# which returns a response object
fire = requests.post(addr, data={'x':x, 'y':y})

# gets HTTP status code
status = fire.status_code

# gets dict of custom headers
headers = fire.headers

# read 'hit' header
hit = headers['hit']

# checks if 'sunk' key exists in dict
if 'sunk' in headers:
    # sets variable to letter corresponding to type of sunken ship
    sunk = headers['sunk']
    print('HTTP{}; Hit={}; Sunk={}'.format(status,hit,sunk))
else:
    print('HTTP{}; Hit={}'.format(status,hit))
