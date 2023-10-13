import http.server
import ssl

# Define the server address and port
server_address = ('localhost', 4443)

# Load SSL/TLS certificates
certfile = r'certificate\server_cert.pem'
keyfile = r'certificate\server_key.pem'

# Configure SSL/TLS settings
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile, keyfile)

# Create a simple HTTP server with SSL/TLS
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print("Server started at", server_address)
httpd.serve_forever()
