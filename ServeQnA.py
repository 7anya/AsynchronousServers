import socket
import threading

HEADER = 64
PORT = 8763
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)


def handle_client1(conn1, addr1, conn2, addr2):  # recives question from client 1, sends question to client 2.
    print(f"[NEW CONNECTION]{addr1} connected ")
    print(f"[NEW CONNECTION]{addr2} connected ")
    connected = True
    while connected:
        msg_length = conn1.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            question = conn1.recv(msg_length).decode(FORMAT)
            print(f"[{addr1}]{question}")
            if question == DISCONNECT_MESSAGE:
                break
            conn2.send(question.encode(FORMAT))
            answer_length = conn2.recv(HEADER).decode(FORMAT)

            if answer_length:
                answer_length = int(answer_length)
                answer = conn2.recv(answer_length).decode(FORMAT)
                print(f"[{addr2}]{answer}")
                if question == DISCONNECT_MESSAGE:
                    break
                conn1.send(answer.encode(FORMAT))

    conn1.close()
    conn2.close()
    # socket.close()


def start():
    server.listen()
    print(f"server is listening on {SERVER}")
    conn2, addr2 = server.accept()  # answer client
    while True:
        conn1, addr1 = server.accept()  # receives quesion from question client
        thread = threading.Thread(target=handle_client1, args=(conn1, addr1, conn2, addr2))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.activeCount() - 1}")


print("[STARTING] server is starting....")
start()
