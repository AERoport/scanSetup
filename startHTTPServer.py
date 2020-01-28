from http.server import HTTPServer, CGIHTTPRequestHandler
port = 8000
server_address = ("", port)
print(server_address)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()