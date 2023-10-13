import http.server
import ssl

class CustomRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the length of the request data
        content_length = int(self.headers['Content-Length'])
        # Read the request data
        response_message = self.rfile.read(content_length).decode('utf-8')

        # Print the received message from the client
        print("Response from client:", response_message)

        # Send a message to the client
        user_input = input("Enter text to send to the client ('q' to quit): ")

        if user_input.lower() == 'q':
            return

        # acknowledging a sended message to the client 
        print("Sent to client:", user_input)

        # Send the response back to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(("Response from server: " + user_input).encode('utf-8'))

# Define the server address and port
server_address = ('localhost', 4443)

# Load SSL/TLS certificates
certfile = r'practical 07\certificate_&_Key\server_cert.pem'
keyfile = r'practical 07\certificate_&_Key\server_key.pem'

# Configure SSL/TLS settings
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile, keyfile)

# Create a custom HTTP server with SSL/TLS
httpd = http.server.HTTPServer(server_address, CustomRequestHandler)
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print("Server started at", server_address)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
