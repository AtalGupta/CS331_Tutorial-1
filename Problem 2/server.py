import socket
import time
import sys
import threading
import multiprocessing

# Server configurations
HOST = '127.0.0.1'  # Localhost
PORT = 12345

def handle_client(client_socket):
    """Handles a single client connection."""
    try:
        data = client_socket.recv(1024).decode()
        if data:
            time.sleep(3)  # Simulating processing delay
            reversed_data = data[::-1]
            client_socket.sendall(reversed_data.encode())
        client_socket.close()
    except Exception as e:
        print(f"Error handling client: {e}")

def single_process_server():
    """Single-process server: handles only one client at a time."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("[Single-Process Server] Listening for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        handle_client(client_socket)

def multi_process_server():
    """Multi-process server: spawns a new process for each client."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("[Multi-Process Server] Listening for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        process.start()
        client_socket.close()

def multi_threaded_server():
    """Multi-threaded server: spawns a new thread for each client."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("[Multi-Threaded Server] Listening for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <single | multi_process | multi_thread>")
        sys.exit(1)

    server_type = sys.argv[1]

    if server_type == "single":
        single_process_server()
    elif server_type == "multi_process":
        multi_process_server()
    elif server_type == "multi_thread":
        multi_threaded_server()
    else:
        print("Invalid server type. Choose from: single, multi_process, multi_thread")
        sys.exit(1)
