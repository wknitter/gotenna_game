import socket
import time
import threading


class ConnectionManager:

    def __init__(self, callback):
        self.callback = callback
        t1 = threading.Thread(target=self.connect, args=())
        t1.start()

    def connect(self):
        mysocket = socket.socket()
        host = socket.gethostbyname(socket.getfqdn())
        port = 9876

        if host == "127.0.1.1":
            import commands
            host = commands.getoutput("hostname -I")
        print("host = " + host)

        # Prevent socket.error: [Errno 98] Address already in use
        mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        mysocket.bind((host, port))

        mysocket.listen(5)

        self.c, addr = mysocket.accept()
        print(f"Connection from {addr} has been established")
        self.c.send(bytes("You're connected Joshy!", "utf-8"))
        while True:
            message = self.c.recv(1024).decode("utf-8")
            self.callback(message)

    def send_message(self, message):
        self.c.send(bytes(message,  "utf-8"))

    def quit(self):
        self.c.send(bytes("Bye!\n", "utf-8"))
        time.sleep(2)
        self.c.close()


