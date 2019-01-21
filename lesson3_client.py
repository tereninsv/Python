import socket
import json
import time
from utils import dict_to_bytes, bytes_to_dict


class Client:

    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password
        self.s = socket.socket()

    def authenticate(self):
        server.send(dict_to_bytes({"action": "authenticate", "time": time.time(),
                                   "user": {"account_name": self.account_name, "password": self.password}}))

    def presence(self, status):
        server.send(dict_to_bytes({"action": "presence", "time": time.time(),
                                   "user": {"account_name": self.account_name, "status": status}}))

    def msg(self):
        to = input('кому:')
        message = input('сообщение:')
        server.send(dict_to_bytes({"action": "msg", "time": time.time(),
                                   "to": to, "from": self.account_name, "encoding": "ascii", "message": message}))

    def quit(self):
        server.send(dict_to_bytes({"action": "quit", "time": time.time(),
                                   "account_name": self.account_name}))
        server.close()
        exit(0)

    def say(self):
        print(self.account_name, self.password)

    def response(self):
        server_response = bytes_to_dict(server.recv).get("response")
        print(server_response)
        return server_response


if __name__ == "__main__":
    server = socket.socket()
    server.connect(('localhost', 7777))

    server_response = ''
    while server_response != '200':
        client = Client(input('введите логин:'), input('введите пароль:'))
        client.authenticate()
        server_response = client.response()

chat = {
    "msg": client.msg,
    "quit": client.quit
}

while True:
    act = input("введите действие:")
    if chat.get(act):
        chat[act]()
    else:
        print('такой команды не существует')
