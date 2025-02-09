import socket
import threading
import multiprocessing

class Server:
    def __init__(self, host='127.0.0.1', port=65432, mode='single'):
        self.host = host
        self.port = port
        self.mode = mode

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"Server started in {self.mode}-mode on {self.host}:{self.port}")

            if self.mode == 'single':
                self.single_process_server(server_socket)
            elif self.mode == 'multi-process':
                self.multi_process_server(server_socket)
            elif self.mode == 'multi-threaded':
                self.multi_threaded_server(server_socket)

    def handle_client(self, conn, addr):
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data or data == '4':
                break
            response = self.process_request(data)
            conn.sendall(response.encode())
        conn.close()

    def process_request(self, request):
        option, value = request.split('|', 1)
        if option == '1':
            return value.swapcase()
        elif option == '2':
            try:
                return str(eval(value))
            except Exception as e:
                return f"Error: {e}"
        elif option == '3':
            return value[::-1]
        else:
            return "Invalid option"

    def single_process_server(self, server_socket):
        while True:
            conn, addr = server_socket.accept()
            self.handle_client(conn, addr)

    def multi_process_server(self, server_socket):
        while True:
            conn, addr = server_socket.accept()
            process = multiprocessing.Process(target=self.handle_client, args=(conn, addr))
            process.start()

    def multi_threaded_server(self, server_socket):
        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else 'single'
    server = Server(mode=mode)
    server.start()
