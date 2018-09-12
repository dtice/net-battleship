from http.server import *

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Running " + str(httpd.server_name) + " on " + str(httpd.server_port) + "...")
    httpd.serve_forever()

run()
