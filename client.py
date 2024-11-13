""" Programmering 2 - Individuell Uppgift: Chatt med Sockets - Silan Aslan """
# Client Side Chat Room

import socket, threading

# Constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# Client socket with IPv4 and TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message() -> None:
    """ Sends a message to the server to broadcasting """
    while True:
        message = input('') #Promt for user input
        client_socket.send(message.encode(ENCODER))

def receive_message() -> None:
    """ Receives an incoming message from the server """
    while True:
        try:
            # Receive an incoming message from the server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if message == 'USERNAME':
                name = input('Welcome! Please choose a username to join the chat: ')
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)

        except:
            # Close the connection with error
            print('An error occurred. Closing the connection...')
            client_socket.close()
            break

# Threads to send and receive messages
receive_thread = threading.Thread(target = receive_message)
send_thread = threading.Thread(target = send_message)

# Starts the client
receive_thread.start()
send_thread.start()



