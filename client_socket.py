import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connecting to {HOST_IP}, port {HOST_PORT}...")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print(f"Connection to {HOST_IP} has been refused. Reconnecting in 4 seconds...")
        time.sleep(4)
    else:
        print(f"Connection to {HOST_IP}, port {HOST_PORT} has been established.")
        print("Type 'q' to quit.")
        break
# ...
while True:
    data_received = s.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    if data_received.decode() == "q":
        break
    print(f"Server : {data_received.decode()}")

    txt_to_send = input("You : ")
    s.sendall(txt_to_send.encode())

s.close()
