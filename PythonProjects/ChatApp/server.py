import socket

chunk = 1024
port = 3000

# create a socket object
# socket is used as entry and exit point of messages
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.AF_INET is used to use ipv4 addresses
# socket.SOCK_DGRAM is used for UDP
# socket.SOCK_STREAM is used for TCP

# ip address will receive the message
hostname = '127.0.0.1'  # this is common for every pc

# used to connect ip address and port
s.bind((hostname, port))

print(f"Server is live on {s.getsockname()}")

# run the server
while True:
    message, clientAdd = s.recvfrom(chunk)
    data = message.decode('ascii')
    print(f'Received from {clientAdd} : {data}')
    message_send = input('Reply: ')
    data_send = message_send.encode('ascii')
    s.sendto(data_send, clientAdd)
