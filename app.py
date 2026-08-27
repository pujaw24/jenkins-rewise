from http.server import HTTPServer, BaseHTTPRequestHandler
#hghfg
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Jenkins + Docker2 CI/CD!</h1>")

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("Server started on port 8000")
server.serve_forever()
