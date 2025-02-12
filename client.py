import socket
import threading
#hiiiii
def receive_messages(sock):
    """Listens for messages from the server and prints them."""
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            print(f"\n[Partner]: {message}")
        except:
            print("Disconnected from server.")
            break

def start_client():
    server_ip = input("Enter server IP: ")  # e.g., "123.45.67.89" or "localhost"
    server_port = 5555
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, server_port))
        print("Connected to server! Start chatting.")
    except:
        print("Failed to connect.")
        return

    # Start thread to listen for messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages
    while True:
        message = input()
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("Connection lost.")
            break

if __name__ == "__main__":
    start_client()
