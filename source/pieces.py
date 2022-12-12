import pygame

class Pawn:
    
    def __init__(self, win, x, y, width, height, colour):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        if self.colour.lower() == "black":
            self.image = pygame.image.load("assets/pieces/blackPieces/bPawn.png")
            self.rsimage = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = pygame.image.load("assets/pieces/whitePieces/wPawn.png")
            self.rsimage = pygame.transform.scale(self.image, (self.width, self.height))
    
    def drawPawn(self):
        self.win.blit(self.rsimage, (self.x, self.y))