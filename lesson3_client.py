import socket
import time
from utils import *


class Client:

    def __init__(self, account_name, password):
        self.account_name = account_name
        self.password = password
        self.s = socket.socket()

    def authenticate(self):
        server.send(dict_to_bytes({"action": "authenticate", "time": time.time(),
                                   "user": {"account_name": self.account_name, "password": self.password}}))
        log_info(log, "authenticate")

    def presence(self, status):
        server.send(dict_to_bytes({"action": "presence", "time": time.time(),
                                   "user": {"account_name": self.account_name, "status": status}}))
        log_info(log, "presence")

    def msg(self):
        to = input('кому:')
        message = input('сообщение:')
        server.send(dict_to_bytes({"action": "msg", "time": time.time(),
                                   "to": to, "from": self.account_name, "encoding": "ascii", "message": message}))
        log_info(log, "msg")
    def quit(self):
        server.send(dict_to_bytes({"action": "quit", "time": time.time(),
                                   "account_name": self.account_name}))
        log_info(log, "quit")
        server.close()
        exit(0)

    def say(self):
        print(self.account_name, self.password)

    def response(self):
        server_response = bytes_to_dict(server.recv).get("response")
        log_info(log, server_response)
        print(server_response)
        return server_response

def server_connect():
    try:
        server = socket.socket()
        server.connect(('localhost', 7777))
    except:
        log_critical(log_client, 'not connect')
    return server


if __name__ == "__main__":
    # log_client = start_log('client')
    server = server_connect()


    server_response = ''
    # log_debug(log_client, 'start auth')
    while server_response != '200':
        client = Client(input('введите логин:'), input('введите пароль:'))
        log = start_log(client.account_name)
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
