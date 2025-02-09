# File Transfer Server

This project is a simple TCP-based File Transfer Server implemented in Python. It allows multiple clients to connect to a central server and perform file-related operations like listing files, reading file contents, uploading, and downloading files. The system uses sockets for network communication and threads to handle multiple clients concurrently.

## Features

- Supports multiple clients simultaneously.
- Allows clients to perform the following operations:
  - **List files**: View all files in the server's directory.
  - **Read file contents**: Retrieve the content of a specified file.
  - **Download files**: Download files from the server to the client.
  - **Upload files**: Upload files from the client to the server.
- Simple command-based interface for clients.
- Basic exception handling for disconnections and file errors.
- **SECURITY FLAW!!!: USERS CAN READ FILES SUCH AS `/etc/passwd`, CAN BE FIXXED MANAGING AND FILTERING USER INPUT**

## How to Use

### Clone the Repository
```bash
git clone https://github.com/jmoreno1852/FT-Server.git
cd FT-Server/
```

### Run the Server
Ensure you have Python installed (version 3.8 or higher), then start the server:

```bash
python main.py
```

The server will start and listen for incoming connections on port 4444 by default.

### Run a Client
Open multiple terminals and run the client:

```bash
python src/client.py
```

You can then interact with the server using the following commands:

- `ls`: List all files in the server's directory.
- `cat <filename>`: Display the contents of a specified file.
- `get <filename>`: Download a file from the server.
- `put <filename>`: Upload a file to the server.


### Example Interaction
1. Client connects to the server.
2. Client runs the `ls` command to view available files.
3. Client uses `get <filename>` to download a file.
4. Client uses `put <filename>` to upload a file to the server. Empty files will not be uploaded.
5. Client disconnects with the `exit` command.

## File Structure

```plaintext
📁 FT-Server/
│── 📁 src/
│   │── server.py   # Contains the main server logic
│   │── client.py   # Contains the client logic
│── main.py         # Entry point to start the server
│── README.md       # Project documentation
```

