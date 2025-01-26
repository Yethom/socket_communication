import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024
SEC_TO_WAIT = 5

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting ({SEC_TO_WAIT}sec) for connection on {HOST_IP}, port {HOST_PORT}...")

s.settimeout(10)
try:
    connection_socket, client_addr = s.accept()
    print(f"Connection from {client_addr} has been established.")
    print("Type 'q' to quit.")
except socket.timeout:
    print(f"No connection on {HOST_IP}, port {HOST_PORT} in {SEC_TO_WAIT} seconds.")
else:
    while True:
        txt_to_send = input("You : ")
        connection_socket.sendall(txt_to_send.encode())
        data_retrieved = connection_socket.recv(MAX_DATA_SIZE)
        if not data_retrieved:
            break
        if data_retrieved.decode() == "q":
            break
        print(f"Client : {data_retrieved.decode()}")

    connection_socket.close()
s.close()
