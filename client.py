import socket
import sys
import requests

# sets coordinates, port, and address according to arguments
port = int(sys.argv[2])
addr = '{}{}:{}'.format("http://",sys.argv[1],port)
x = int(sys.argv[3])
y = int(sys.argv[4])
guess_board = [['0' for q in range(10)] for p in range(10)]

# attempts post request at given address with given payload
# which returns a response object
fire = requests.post(addr, data={'x':x, 'y':y})

# gets HTTP status code
status = fire.status_code

# gets dict of custom headers
headers = fire.headers

# read 'hit' header
hit = headers['hit']

file = open("opponent_board.txt", "r")
guess_board = file.readlines()
print(x,y)
print(hit)
if(hit == '1'):
    temp = guess_board[x]
    tempL = list(temp)
    tempL[y] = "X"
    temp = ''.join(tempL)
    guess_board[x] = temp
else:
    temp = guess_board[x]
    tempL = list(temp)
    #print(tempL)
    tempL[y] = "M"
    temp = ''.join(tempL)
    guess_board[x] = temp

# checks if 'sunk' key exists in dict
if 'sunk' in headers:
    # sets variable to letter corresponding to type of sunken ship
    sunk = headers['sunk']
    print('HTTP{}; Hit={}; Sunk={}'.format(status,hit,sunk))
else:
    print('HTTP{}; Hit={}'.format(status,hit))

f = open("opponent_board.txt", "w")
f.writelines(list(guess_board))
f.close()
