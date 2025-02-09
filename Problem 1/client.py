import socket

def client_program():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        while True:
            print("\nMenu:")
            print("1. Change the case of a string")
            print("2. Evaluate a mathematical expression")
            print("3. Find the reverse of a given string")
            print("4. Exit the program")
            
            choice = input("Enter your choice: ")

            if choice == '4':
                client_socket.sendall(choice.encode())
                break

            value = input("Enter the input value: ")
            client_socket.sendall(f"{choice}|{value}".encode())

            response = client_socket.recv(1024).decode()
            print(f"Response from server: {response}")

if __name__ == "__main__":
    client_program()
