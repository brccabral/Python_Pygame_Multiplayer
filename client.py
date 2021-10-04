# pip install pygame
import pygame
from game import Game
from network import Network
from player import Player

width = 700
height = 700

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redrawWindow(win:pygame.Surface, game:Game, player:Player):
    win.fill((128,128,128))
    pass

def main():
    pass

main()