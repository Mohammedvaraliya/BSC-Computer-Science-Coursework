## Practical 07

## Problem Statement

* Web Security with SSL/TLS:
* Configure and implement secure web communication using SSL/TLS protocols, including certificate management and secure session establishment.

---

## Setup and Prerequisites

1. **Install OpenSSL**:
   - Download and install OpenSSL from [OpenSSL Win64 Website](https://slproweb.com/products/Win32OpenSSL.html).
   
2. **Add OpenSSL to Your Environment Variables**:
   - Add the OpenSSL binary directory to your system's PATH:
     ```bash
     C:\Program Files\OpenSSL-Win64\bin
     ```

## Generating SSL/TLS Certificates

Generate a new SSL/TLS certificate specifically for the hostname **localhost** using the OpenSSL command:
```bash
openssl req -x509 -newkey rsa:4096 -keyout server_key.pem -out server_cert.pem -days 365 -subj "/CN=localhost"
```

Follow the prompts to enter the required information.

## Running the Secure Web Server

1. Open a Command Prompt.

2. Navigate to the directory containing the Python scripts and the generated certificates.

3. Run the server script:
   ```bash
   python secure_web_server.py
   ```

   expected output:
   ```bash
   Enter PEM pass phrase:
   Server started at ('localhost', 4443)
   ```

4. Enter the PEM pass phrase when prompted.

5. The server will start at `https://localhost:4443`.

## Running the Secure Web Client

1. Open another Command Prompt.

2. Navigate to the directory containing the Python scripts and the generated certificates.

3. Run the client script:
   ```bash
   python secure_web_client.py
   ```

   expected output:
   ```html
   Response from server:
   <!DOCTYPE HTML>
   <html lang="en">
   <head>
   <meta charset="utf-8">
   <title>Directory listing for /</title>
   </head>
   <body>
   <h1>Directory listing for /</h1>
   <hr>
   <ul>
   <li><a href="certificate/">certificate/</a></li>
   <li><a href="README.md">README.md</a></li>
   <li><a href="secure_web_client.py">secure_web_client.py</a></li>
   <li><a href="secure_web_server.py">secure_web_server.py</a></li>
   </ul>
   <hr>
   </body>
   </html>
   ```

4. You should receive a response from the server.