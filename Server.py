from cryptography.fernet import Fernet
import socket


def cryptography():
    # Create a key for encryption
    key = Fernet.generate_key()
    file = open('key.txt', 'wb')
    file.write(key)
    file.close()
    return key


def create_socket(ip, port):
    # Create a socket for communication between Server and Client
    s.bind((ip, port))
    s.listen(2)
    print('Server is listening')


# Create a socket object
s = socket.socket()
running = True

create_socket('127.0.0.1', 12345)
Key = cryptography()

while running:
    c, addr = s.accept()
    c.send('Password:'.encode())
    password = c.recv(1024).decode()
    if password == Key.decode():
        print(f'get connected to {addr}')
        while running:
            # Chat with the client and send "quit" if you want to disconnect
            message_to_client = input('message:')
            c.send(message_to_client.encode())
            if message_to_client == 'quit':
                running = False
            else:
                message_from_client = c.recv(1024).decode()
                print(f'Message from client: {message_from_client}')
                if message_from_client == 'quit':
                    running = False
    else:
        # If password is wrong close connection
        c.send('Lost Connection'.encode())

# Close connection
c.close()
