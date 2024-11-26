""" Programmering 2 - Individuell Uppgift: Chatt med Sockets - Silan Aslan """
# Server Side Chat Room

import socket, threading

# Constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# Server socket with IPv4 and TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Dictionary to store connected client sockets and their names
clients = {}


def broadcast_message(message: bytes) -> None:
    """ Sends a message to ALL clients connected to the server"""
    for client, _ in clients.items():
        client.send(message)


def receive_message(client_socket) -> None:
    """ Receives an incoming message from a specific client and forward the message to be broadcast """
    name = clients[client_socket]
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            if not message:
                # Handle normal disconnection
                del clients[client_socket]
                client_socket.close()

                # Inform all users that the client has left the chat
                broadcast_message(f'***{name} has left the chat due to a connection error!***'.encode(ENCODER))
                return

            message = f'{name}: {message}'.encode(ENCODER)  # Encodes to be used for broadcasting
            broadcast_message(message)

        except ConnectionResetError:
            # Handle case where connection was forcibly closed by the remote host and remove the client
            del clients[client_socket]
            client_socket.close()

            # Inform all user that a user has encountered an error
            broadcast_message(f'***{name} has left the chat due to a connection error!***'.encode(ENCODER))
            return

        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")
            del clients[client_socket]
            client_socket.close()
            broadcast_message(f'***{name} has errored out of the chat!***'.encode(ENCODER))
            return


def connect_client() -> None:
    """ Connects an incoming client to the server """
    while True:
        client_socket, client_adress = server_socket.accept()
        print(f'Connected with {client_adress}...')

        # Sends a NAME flag to prompt the client for their name
        client_socket.send('USERNAME'.encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        # Add the new client and their name to the dictionary
        clients[client_socket] = client_name

        # Informing about the new client and welcome them
        print(f'New client: {client_name}\n')  # The server

        # Welcome ASCII art sent to the new client
        welcome_art = r"""

_________________________________________________
            ________________________             |\
           |                        |            | \
______     |     W E L C O M E      |            |  \
      |    |                        |            |   \
      |    |    TO  MY CHATROOM:    |            |
      |    |                        |            |
      |    |     S H I C H A T      |            |   |\
      |[]  |________________________|            |   | \
   () |                                          |   |  \
      |                           \\\\  ____     |   |\ |
      |                           ( oo |\___\    |   | \|
      |                            \-/ ||___|    |   \\ |
      |                           (/_\)/____\_   |    \\|
______|__________________________ |\  ||_____|\__|
                                  | \__________\  \
                                  \ |          |   \
                                   \|__________|    \
        """
        client_socket.send(welcome_art.encode(ENCODER))

        # Broadcast that the new user has joined the chat
        broadcast_message(f'\n***{client_name} has joined the chat!***\n'.encode(ENCODER))  # All in the chat

        welcome_message = f'''\nWelcome to Shichat, {client_name}!
Enjoy your stay!
Feel free to start typing your message below:\n'''

        client_socket.send(welcome_message.encode(ENCODER))  # The individual client

        # Starts thread for receiving messages from the new client.
        # Uses daemon for automatically ending the thread with the main program.
        receive_thread = threading.Thread(target=receive_message, daemon=True, args=(client_socket,))
        receive_thread.start()


# Starts the server and shut it down with user interruption.
print('Server is listening for incoming connections...\n')
try:
    connect_client()
except KeyboardInterrupt:
    print('Server is shutting down...')
finally:
    server_socket.close()
    print('Server has been closed!')

