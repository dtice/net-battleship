from http.server import *
from http.client import *
import sys
import requests

# get port and name of board file from arguments
port = int(sys.argv[1])
board = sys.argv[2]
w, h = 10, 10;
board = [[0 for x in range(w)] for y in range(h)]
cCount = 0
bCount = 0
rCount = 0
sCount = 0
dCount = 0
#reads the txt file into an array that the server can read from
i = 0;
with open(sys.argv[2], 'r') as f:
	while (i != 10):
		next = f.readline()
		next = next.rstrip()
		board[i] = next
		i = i+1;

for row in board:
    #line = list(board[i])
    for y in row:
        if(y == 'C'):
            cCount += 1;
        if(y == 'B'):
            bCount += 1;
        if(y == 'R'):
            rCount += 1;
        if(y == 'S'): 
            sCount += 1;
        if(y == 'D'): 
            dCount += 1;

        

print(cCount)
        
        

# client_handler uses BaseHTTPRequestHandler to handle POST requests
class client_handler(SimpleHTTPRequestHandler):
    def _set_headers(self, hit, sunk, dupe, ib):
        # if the player has never hit this spot
        if dupe == 0:
            # if the salvo is in-bounds
            if ib == 1:
                # if the salvo hits a boat
                if hit == 1:
                    self.send_response(200)
                    self.send_header('hit', '1')
                    # if the salvo sinks a boat
                    if sunk != 'X':
                        self.send_header('sunk',sunk)
                else:
                    self.send_response(200)
                    self.send_header('hit', '0')
            else:
                self.send_response(404)
                self.send_header('hit', '0')
        else:
            self.send_response(410)
            self.send_header('hit', '0')
        self.end_headers()

    def do_POST(self):
        # gets the length of the custom headers
        s = int(self.headers.get('content-length')[0])
        # reads the custom headers
        coords = self.rfile.read(s).decode('utf-8')

        # string manipulation
        x,y = coords.split("&")
        x = x.split("=")[1]
        y = y.split("=")[1]

        # prints coordinates
        # print("Received coordinates: X: {}, Y: {}".format(x,y))

        # checks board using given coordinates
        hit,sunk,dupe,ib = check_board(x,y)

        # sets headers on packet
        self._set_headers(hit,sunk,dupe,ib)

	def do_GET(self):
		self.send_response(200)
		self.end_headers()

# checks board and sets hit, sunk, dupe, and ib according to coordinates and boat placement
def check_board(x, y):
    hit,sunk,dupe,ib = 0, 'X', 0, 0
    global cCount
    global bCount
    global rCount
    global sCount
    global dCount
    x = int(x)
    y = int(y)
    if(0 <= x <= 10 and 0 <= y <= 10):
        target = board[x][y]
        ib = 1
        if(target == "X"):
            dupe = 1
        if(target != "_"):
            hit = 1
        temp = board[x]
        tempL = list(temp)
        if(target == 'C'):
            cCount -= 1;
        if(target == 'B'):
            bCount -= 1;
        if(target == 'R'):
            rCount -= 1;
        if(target == 'S'): 
            sCount -= 1;
        if(target == 'D'): 
            dCount -= 1;
        tempL[y] = "X"
        temp = ''.join(tempL)
        board[x] = temp
        for i in board:
	        print(i)
        if(cCount == 0):
            sunk = 'C';
            cCount = -1;
        if(bCount == 0):
            sunk = 'B';
            bCount = -1;
        if(rCount == 'R'):
            sunk = 'R';
            rCount = -1;
        if(sCount == 'S'): 
            sunk = 'S';
            sCount = -1;
        if(dCount == 'D'): 
            sunk = 'D';
            dCount -1;
    return hit,sunk,dupe,ib

# runs the server
def run(server_class=HTTPServer, handler_class=client_handler, port=port):
    # sets server address and port
    server_address = ('127.0.0.1', port)
    # initializes server class
    httpd = server_class(server_address, handler_class)
    print('Starting server on port ', port)
    # starts server
    httpd.serve_forever()

run()
