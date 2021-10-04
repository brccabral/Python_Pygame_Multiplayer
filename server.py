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

connected = set()
# multiple games will be based on id
games = {}
idCount = 0

def threaded_client(conn:sk, player):
    pass

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn))