import socket
import json
import time


def client_action(type, user, to='', misk=''):
    if type == "authenticate":
        server.send(json.dumps({"action": type, "time": time.time(),
                                "user": {"account_name": user, "password": misk}},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))

    if type == "presence":
        server.send(json.dumps({"action": type, "time": time.time(),
                                "user": {"account_name": user, "status": misk}},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))

    if type == "msg":
        server.send(json.dumps({"action": type, "time": time.time(),
                                "to": to, "from": user, "encoding": "ascii", "message": misk},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))

    if type == "quit":
        server.send(json.dumps({"action": type, "time": time.time(),
                                "account_name": user},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))


def client_response():
    pass


if __name__ == "__main__":

    server = socket.socket()
    server.connect(('localhost', 7777))
    login_response = 0
    while login_response != '200':
        username = input('введите логин:')
        password = input('введите пароль:')
        client_action("authenticate", username, '', password)
        login_response = eval(server.recv(1024).decode("UTF-8")).get("response")
        print(login_response)
    client_action("presence", username, "Yep, I am here!")

    while True:
        action = input('введите команду:')
        if action == 'quit':
            client_action(action, username)
            print('Вы покинули чат')
            break
        if action == 'msg':
            client_action(action, username, input('кому сообщение:'), input('введите текст:'))
