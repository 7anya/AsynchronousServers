import socket  # Import socket module

HEADER = 64
PORT = 5678
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
answers = {"1": "one", "2": "two", "3": "three"}
# key=""

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # key=client.recv(2048).decode(FORMAT)
    # print(key)


# key = "1"
# send("HELLO WORLD")
key=client.recv(2048).decode(FORMAT)
print(key)
send(answers[key])
print(answers[key])
# send(DISCONNECT_MESSAGE)
