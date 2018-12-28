import socket
import json
import time


class ClientAction:

    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password

    def authenticate(self):
        server.send(json.dumps({"action": "authenticate", "time": time.time(),
                                "user": {"account_name": self.account_name, "password": self.password}},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))

    def presence(self, status):
        server.send(json.dumps({"action": "presence", "time": time.time(),
                                "user": {"account_name": self.account_name, "status": status}},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))

    def msg(self):
        to = input('кому:')
        message = input('сообщение:')
        server.send(json.dumps({"action": "msg", "time": time.time(),
                                "to": to, "from": self.account_name, "encoding": "ascii", "message": message},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))

    def quit(self):
        server.send(json.dumps({"action": "quit", "time": time.time(),
                                "account_name": self.account_name},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))
        server.close()
        exit(0)

    def say(self):
        print(self.account_name, self.password)

    def response(self):
        server_response = eval(server.recv(1024).decode("UTF-8")).get("response")
        print(server_response)
        return server_response


if __name__ == "__main__":
    server = socket.socket()
    server.connect(('localhost', 7777))

    server_response = ''
    while server_response != '200':
        client = ClientAction(input('введите логин:'), input('введите пароль:'))
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