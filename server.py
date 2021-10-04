from os import error
import pickle
import socket
from _socket import socket as sk
from _thread import *
import sys

from player import Player

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

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,255,0))]

def threaded_client(conn:sk, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            # 2048 bytes to receive
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                
                print("Received: ", data)
                print("Sending: ", reply)
            conn.sendall(pickle.dumps(reply))
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