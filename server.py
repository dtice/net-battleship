from http.server import *
from http.client import *
import sys
import requests

# get port and name of board file from arguments
port = int(sys.argv[1])
board = sys.argv[2]

# client_handler uses BaseHTTPRequestHandler to handle POST requests
class client_handler(BaseHTTPRequestHandler):
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
        y,x = coords.split("&")
        x = x.split("=")[1]
        y = y.split("=")[1]

        # prints coordinates
        # print("Received coordinates: X: {}, Y: {}".format(x,y))

        # checks board using given coordinates
        hit,sunk,dupe,ib = check_board(x,y)

        # sets headers on packet
        self._set_headers(hit,sunk,dupe,ib)

# checks board and sets hit, sunk, dupe, and ib according to coordinates and boat placement
def check_board(x, y):
    hit,sunk,dupe,ib = 0, 'X', 0, 0
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
