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

4. Enter the PEM pass phrase when prompted.

5. Start the communication.

## Running the Secure Web Client

1. Open another Command Prompt.

2. Navigate to the directory containing the Python scripts and the generated certificates.

3. Run the client script:
   ```bash
   python secure_web_client.py
   ```

4. Start the communication.


## Output

1. Expected output from server's terminal:
   ```bash
   Enter PEM pass phrase:
   Server started at ('localhost', 4443)
   Response from client: hello
   Enter text to send to the client ('q' to quit): Hello i am server
   Sent to client: Hello i am server
   127.0.0.1 - - [13/Oct/2023 19:30:39] "POST / HTTP/1.1" 200 -
   Response from client: Hello i am client
   Enter text to send to the client ('q' to quit): this is server speaking
   Sent to client: this is server speaking
   127.0.0.1 - - [13/Oct/2023 19:31:32] "POST / HTTP/1.1" 200 -
   Response from client: this is client speaking
   Enter text to send to the client ('q' to quit): 
   ```
   
2. Expected output from client's terminal:
   ```bash
   Enter text to send to the server ('q' to quit): hello
   Sent to server: hello
   Response from server: Hello i am server
   Enter text to send to the server ('q' to quit): Hello i am client
   Sent to server: Hello i am client
   Response from server: this is server speaking
   Enter text to send to the server ('q' to quit): this is client speaking
   Sent to server: this is client speaking
   ```