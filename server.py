from os import error
import socket
from _socket import socket as sk
from _thread import *
import sys

# Win = ipconfig
# Ubuntu = ip a
server = "192.168.0.23"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started!")

def read_pos(pos_str:str):
    split_str = pos_str.split(",")
    return int(split_str[0]), int(split_str[1])

def make_pos(tup):
    return str(tup[0])+","+str(tup[1])

pos = [(0,0),(100,100)]

def threaded_client(conn:sk, player):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # bytes to receive
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
            break
    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer += 1