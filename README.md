# Keylogger Server

🔒 A real-time keylogger server application built with Python that captures keystrokes from a client and displays them in a terminal-style GUI. This project is designed for educational purposes to demonstrate keylogging and information security concepts.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Disclaimer](#disclaimer)
- [License](#license)

## Features

- Real-time key capture and logging from a client.
- User-friendly GUI with a "hacker console" aesthetic.
- Color-coded messages for easy differentiation (logs, connections, errors).
- Timestamp for each logged key, providing context.
- Option to clear logs for convenience.
- Simple server-client architecture using TCP sockets.

## Technologies Used

- Python 3.x
- Tkinter (for GUI)
- Socket programming (for client-server communication)
- Logging module (for saving logs to a file)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Fuzail-Raza/Keylogger-Server.git
   cd Keylogger-Server
   ```

2. **Install dependencies:**

   Ensure you have Python 3.x installed. You may not need additional libraries, as the required modules are included in the standard library. However, it's a good idea to create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

1. **Start the server:**
   - Run the server script from your terminal:

   ```bash
   python server.py
   ```

   The GUI will open, and the server will start listening for incoming connections.

2. **Run the client:**
   - You need a corresponding client application that sends keystrokes to the server. Make sure the client connects to the server's IP address and port specified in the server code.

3. **View captured keystrokes:**
   - As the client sends keystrokes, they will be displayed in real-time in the server GUI with timestamps.

4. **Clear the logs:**
   - Click the "Clear Log" button in the GUI to remove all displayed logs.

## Code Structure

- `server.py`: The main file containing the server implementation.
  - Sets up a socket server that listens for connections.
  - Captures and logs keystrokes in a GUI interface.
- `requirements.txt`: List of dependencies (if any in the future).

## Disclaimer

This keylogger application is intended for educational purposes only. Do not use it maliciously or without proper authorization. Unauthorized keylogging is illegal and unethical. Always respect the privacy and consent of others.
