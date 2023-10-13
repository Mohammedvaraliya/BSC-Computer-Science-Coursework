import urllib.request
import ssl

# Define the URL to fetch
url = "https://localhost:4443/"

# Create an SSL context with certificate validation
ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(cafile=r'certificate\server_cert.pem')  # Load the server certificate

# Fetch the URL using an HTTPS request
try:
    with urllib.request.urlopen(url, context=ssl_context) as response:
        print("Response from server:")
        print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("Error:", e.reason)
