import socket  # Import socket module

HEADER = 64
PORT = 8763
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
answers = {"1": "one", "2": "two", "3": "three"}


def send(msg):
    print("eee" + msg)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    key = client.recv(2048).decode(FORMAT)
    print(key)
    send(answers[key])
    print(answers[key])
