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
from http.server import *
from http.client import *
import sys
import requests

port = int(sys.argv[1])
board = sys.argv[2]

class client_handler(BaseHTTPRequestHandler):
    def _set_headers(self, hit, sunk, dupe, ib):
        if dupe == 0:
            if ib == 1:
                if hit == 1:
                    self.send_response(200)
                    self.send_header('hit', '1')
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
        s = int(self.headers.get_all('content-length')[0])
        coords = self.rfile.read(s).decode('utf-8')
        y,x = coords.split("&")
        x = x.split("=")[1]
        y = y.split("=")[1]
        print("Received coordinates: X: {}, Y: {}".format(x,y))
        hit,sunk,dupe,ib = check_board(x,y)
        self._set_headers(hit,sunk,dupe,ib)

def check_board(x, y):
    hit,sunk,dupe,ib = 1, 'D', 0, 1
    return hit,sunk,dupe,ib

def run(server_class=HTTPServer, handler_class=client_handler, port=port):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port ', port)
    httpd.serve_forever()

run()
