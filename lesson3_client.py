import socket
import json
import time


# def server_connect():
#     server = socket.socket()
#     server.connect(('localhost', 7777))
#     return server


def client_action(type, user, password):
    if type == "authenticate":
        server.send(json.dumps({"action": type, "time": time.time(),
                                "user": {"account_name": user, "password": password}},
                               sort_keys=True, indent=4).encode("UTF-8"))
    if type == "presence":
        server.send(json.dumps({"action": type, "time": time.time(),
                                "user": {"account_name": user, "status": password}},
                               sort_keys=True, indent=4).encode("UTF-8"))




def response():
    pass


if __name__ == "__main__":
    server = socket.socket()
    server.connect(('localhost', 7777))

    client_action("authenticate", "user123", "paswd123")
    print(server.recv(1024).decode("UTF-8"))
    client_action("presence", "user123", "Yep, I am here!")



# db_users = {"user123": "paswd123", "user1": "paswd1", "testtest": {"test": "123", "test1": "456"}}
#
# # print(db_users.keys())
# #
# # if 'user1' in db_users.keys():
# #     print('yes')
# print(db_users.get("testtest").get("test"))
