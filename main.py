import os
import sys
import socketserver
from http.server import SimpleHTTPRequestHandler

class LiveGameServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # A lightweight backend ping responder that stays awake
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b"Jujutsu Arena Backend Online!")

if __name__ == "__main__":
    # Dynamically read whatever random port Railway assigns
    port = int(os.environ.get("PORT", 8080))
    print(f"Server domain expanding on port {port}", flush=True)
    
    # Force the server to listen to all external cloud traffic (0.0.0.0)
    with socketserver.TCPServer(("0.0.0.0", port), LiveGameServer) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
