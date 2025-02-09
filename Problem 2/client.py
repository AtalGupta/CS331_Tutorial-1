import socket
import sys

SERVER_HOST = '127.0.0.1'  # Server IP
SERVER_PORT = 12345        # Server Port

def client():
    try:
        # Create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Get input from user
        message = input("Enter a string to send: ")

        # Send the message to the server
        client_socket.sendall(message.encode())

        # Receive the reversed string from the server
        response = client_socket.recv(1024).decode()
        print(f"Reversed string from server: {response}")

        # Close the connection
        client_socket.close()
    except Exception as e:
        print(f"Client error: {e}")

if __name__ == "__main__":
    client()
