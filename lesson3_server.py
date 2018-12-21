import socket
import json
import time


def action():
    pass


def server_response(code,alert):
    client.send(json.dumps({"response": code, "alert": alert}, indent=4).encode("UTF-8"))





db_users = {"user123": "paswd123", "user1": "paswd1"}
db_users_online = []

server = socket.socket()
server.bind(('', 7777))
server.listen(5)
client, adr = server.accept()

client_action = eval(client.recv(1024).decode("UTF-8"))

if client_action.get("action") == "authenticate":
    # user = client_action.get('user', '')

    if client_action.get('user').get("account_name") in db_users.keys():
        if client_action.get('user').get('password') == db_users.get(client_action.get('user').get("account_name")):
            print("Авторизация успешна")
            if client_action.get('user').get("account_name") in db_users_online:
                server_response("409", "Someone is already connected with the given user name")

            else:
                db_users_online.append(client_action.get('user').get("account_name"))
                server_response("200", "authorization succes")

        else:
            client.send('неверный логин/пароль'.encode("UTF-8"))
    else:
        client.send('неверный логин/пароль'.encode("UTF-8"))
print(server.recv(1024).decode("UTF-8"))