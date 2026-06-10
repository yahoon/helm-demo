import http.server
import threading

class Handler8081(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"i am 8081")
    def log_message(self, format, *args):
        pass

class Handler8082(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"i am 8082")
    def log_message(self, format, *args):
        pass

def run(port, handler):
    http.server.HTTPServer(("0.0.0.0", port), handler).serve_forever()

threading.Thread(target=run, args=(8081, Handler8081), daemon=True).start()
threading.Thread(target=run, args=(8082, Handler8082)).start()
