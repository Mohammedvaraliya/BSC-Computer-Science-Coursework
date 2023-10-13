import urllib.request
import ssl

# Define the URL to fetch
url = "https://localhost:4443/"

# Create an SSL context with certificate validation
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(cafile=r'practical 07\certificate_&_Key\server_cert.pem')  # Load the server certificate

try:
    while True:
        user_input = input("Enter text to send to the server ('q' to quit): ")
        
        if user_input.lower() == 'q':
            break

        print("Sent to server:", user_input)
        
        # Encode the input as bytes
        user_input_bytes = user_input.encode('utf-8')
        
        # Create a POST request and send the input as the request body
        req = urllib.request.Request(url, data=user_input_bytes, method='POST')
        
        try:
            with urllib.request.urlopen(req, context=ssl_context) as response:
                print(response.read().decode('utf-8'))
        except urllib.error.URLError as e:
            print("Error:", e.reason)

except KeyboardInterrupt:
    print("Client disconnected.")
