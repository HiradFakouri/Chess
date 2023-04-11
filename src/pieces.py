import pygame

class Pawn:
    
    def __init__(self, win, x, y, width, height, colour, spawnDiffrence=79):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        self.pawnDiffrence = spawnDiffrence
        
        self.maxX = self.x + 77.5
        self.maxY = self.y + 77 
        self.selected = False

        self.pawns = []

        if self.colour.lower() == "black":
            self.image = pygame.image.load("assets/pieces/blackPieces/bPawn.png")
            self.rsimage = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = pygame.image.load("assets/pieces/whitePieces/wPawn.png")
            self.rsimage = pygame.transform.scale(self.image, (self.width, self.height))
    
    def drawPawn(self):
        self.win.blit(self.rsimage, (self.x, self.y))

    def select(self):
        self.mouse_pos = pygame.mouse.get_pos()
        #print(self.mouse_pos)
        if ((self.mouse_pos[0] >= self.x and self.mouse_pos[0] <= self.maxX) and (self.mouse_pos[1] >= self.y and self.mouse_pos[1] <= self.maxY)) and pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            self.selected = True
            #pygame.draw.line(self.win, "red", (35.5, 553), (112, 553))
            print("selected")
            print("#")
            

class Rook:

    def __init__(self, win, x, y, width, height, colour, spawnDiffrence=0):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.pawnDiffrence = spawnDiffrence

        if self.colour.lower() == "black":
            self.image = pygame.image.load("assets/pieces/blackPieces/bRook.png")
            self.rsimage = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = pygame.image.load("assets/pieces/whitePieces/wRook.png")
            self.rsimage = pygame.transform.scale(self.image, (self.width, self.height))

    def drawRook(self):
        self.win.blit(self.rsimage, (self.x, self.y))

    