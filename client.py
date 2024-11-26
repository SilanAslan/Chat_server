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

# Threads to receive messages, daemon for automatically ending the thread with the main program.
receive_thread = threading.Thread(target = receive_message, daemon = True)
receive_thread.start()

# Sends message in the main thread and closes the connection with exception or user interruption
try:
    send_message()
except(Exception, KeyboardInterrupt):
    print('Closing the connection...')
    client_socket.close()
