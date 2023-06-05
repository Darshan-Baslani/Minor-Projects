import socket

chunk = 1024
port = 3000
host_name = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    s.connect((host_name, port))
    send_message = input('Enter message: ')
    send_data = send_message.encode('ascii')
    s.send(send_data)

    message = s.recv(chunk)
    data = message.decode('ascii')
    print(f'Darshan says {data}')
