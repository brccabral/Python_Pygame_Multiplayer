import pickle
import socket
from _socket import socket as sk
from _thread import start_new_thread
from game import Game


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(("10.254.254.254", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


# Win = ipconfig
# Ubuntu = ip a
server = get_ip()
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


def threaded_client(conn: sk, playerIndex, gameId):
    global idCount
    conn.send(str.encode(str(playerIndex)))
    reply = ""
    while True:
        try:
            # data can be three actions: reset, get, move
            data = conn.recv(4096).decode()

            # check if game still exists
            if gameId in games:
                game: Game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(playerIndex, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except Exception as e:
            print(e)
            break

    print("Lost connection")

    # if both players close, the first player
    # will delete the game before the other player
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except Exception:
        pass

    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    playerIndex = 0
    # with 10 players we need 5 games
    gameId = (idCount - 1) // 2
    # if id is odd, it means we need a new Game
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        playerIndex = 1

    start_new_thread(threaded_client, (conn, playerIndex, gameId))
