from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        subprocess.Popen(['python', 'HeartMove.py'])
        self.wfile.write("¡Script de Python ejecutado!")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Servidor corriendo en el puerto 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()