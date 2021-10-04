# pip install pygame
import pygame
from game import Game
from network import Network
from player import Player

width = 700
height = 700

pygame.font.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win: pygame.Surface):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        cx = self.x + round(self.width/2) - round(text.get_width()/2)
        cy = self.y + round(self.height/2) - round(text.get_height()/2)
        win.blit(text, (cx, cy))
    
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= (self.x + self.width) and self.y <= y1 <= (self.y + self.height):
            return True
        else:
            return False

def redrawWindow(win:pygame.Surface, game:Game, player:Player):
    win.fill((128,128,128))
    pass

def main():
    pass

main()