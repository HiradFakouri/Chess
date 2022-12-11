import pygame

class Board:

    def __init__(self, win, x, y, width, height):
       self.win = win
       self.x = x
       self.y = y
       self.width = width
       self.height = height
              
       self.image = pygame.image.load("assets/board/board_plain_01.png")
       self.rsimage = pygame.transform.scale(self.image, (self.width, self.width))
    
    def drawBoard(self):
        self.win.blit(self.rsimage, (self.x, self.y))
       
        
