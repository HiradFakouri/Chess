import pygame
import board

class Pages:

    def __init__(self, size, caption, FPS, bgcolour=(0, 0, 0)):
        self.size = size
        self.caption = caption
        self.FPS = FPS
        self.bgcolour = bgcolour
        
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

        self.clock = pygame.time.Clock()

        self.board = board.Board(self.win, 0, 50, 700, 700)

    def localMultyplayer(self):

        def draw():
            self.win.fill(self.bgcolour)
            
            self.board.drawBoard()

            pygame.display.update()

        running = True
        while running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False 
            
            draw()