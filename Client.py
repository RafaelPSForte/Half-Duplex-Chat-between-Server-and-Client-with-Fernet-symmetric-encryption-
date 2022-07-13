import socket


def get_key():
    # Get a key for decryption
    file = open('key.txt', 'rb')
    key = file.read()
    file.close()
    print(f'The access key is: {key.decode()}')
    return key


def connect_to_socket(ip, port):
    # Connect to Server
    s.connect((ip, port))


# Create a socket object
s = socket.socket()

connect_to_socket('127.0.0.1', 12345)
key = get_key()
running = True

while running:
    # Put the key to connect to the server
    print(s.recv(1024).decode())
    password = input('')
    s.sendall(password.encode())
    if password == key.decode():
        print('connected to server')
        while running:
            # Chat with the server and send "quit" if you want to disconnect
            message_from_server = s.recv(1024).decode()
            print(f'Message from Server: {message_from_server}')
            if message_from_server == 'quit':
                running = False
            else:
                message_to_server = input('message:')
                s.sendall(message_to_server.encode())
                if message_to_server == 'quit':
                    running = False
    else:
        # If password is wrong close connection
        print(s.recv(1024).decode())
        break

# Close connection
s.close()
