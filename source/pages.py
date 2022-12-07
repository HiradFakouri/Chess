import pygame
import board

class Pages:

    def __init__(self, size, caption, FPS):
        self.size = size
        self.caption = caption
        self.FPS = FPS
        
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

        self.clock = pygame.time.Clock()

        self.board = board.Board()

    def localMultyplayer(self):

        def draw():
            self.win.blit(self.board.image, (0,0))

            pygame.display.update()

        running = True
        while running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False 