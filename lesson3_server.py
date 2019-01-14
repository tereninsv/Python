import socket
import json
import time


def action(type):
    if type == "probe":
        server.send(json.dumps({"action": type, "time": time.time()},
                               sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))


def server_response(code, alert):
    client.send(
        json.dumps({"response": code, "alert": alert}, sort_keys=True, ensure_ascii=False, indent=4).encode("UTF-8"))


if __name__ == "__main__":

    db_users = {"user123": "paswd123", "user1": "paswd1", "1": "1"}
    db_users_online = []

    server = socket.socket()
    server.bind(('', 7777))
    server.listen(5)
    client, adr = server.accept()

    while True:
        client_action = eval(client.recv(1024).decode("UTF-8"))
        if not client_action:
            continue

        if client_action.get("action") == "authenticate":
            if client_action.get('user').get("account_name") in db_users.keys():
                if client_action.get('user').get('password') == db_users.get(
                        client_action.get('user').get("account_name")):
                    print("Авторизация успешна")
                    if client_action.get('user').get("account_name") in db_users_online:
                        server_response("409", "Someone is already connected with the given user name")

                    else:
                        db_users_online.append(client_action.get('user').get("account_name"))
                        server_response("200", "Необязательное сообщение/уведомление")

                else:
                    server_response("402", "This could be wrong password or no account with that name")
            else:
                server_response("402", "This could be wrong password or no account with that name")

        if client_action.get("action") == "presence":
            print("Yep, I am here!")

        if client_action.get("action") == "msg":
            print(f'сообщение для {client_action.get("to")}: {client_action.get("message")}')

        if client_action.get("action") == "quit":
            print(f'пользователь {client_action.get("account_name")} покинул чат')
            db_users_online.remove(client_action.get("account_name"))
