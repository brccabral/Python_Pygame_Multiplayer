# pip install pygame
import pygame
from network import Network

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.update()
    
    def update(self):
        self.rect = (self.x,self.y,self.width,self.height)

def read_pos(pos_str:str):
    split_str = pos_str.split(",")
    return int(split_str[0]), int(split_str[1])

def make_pos(tup):
    return str(tup[0])+","+str(tup[1])

def redrawWindow(win:pygame.Surface,player:Player,player2:Player):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,0,0))

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2.x, p2.y = read_pos(n.send(make_pos((p.x, p.y))))
        p2.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        p.move()
        redrawWindow(win, p)

main()