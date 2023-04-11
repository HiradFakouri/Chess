import pygame
import board
import pieces

class Pages:

    def __init__(self, size, caption, FPS, square_size, bgcolour=(0, 0, 0)):
        self.size = size
        self.caption = caption
        self.FPS = FPS
        self.bgcolour = bgcolour
        self.squre_size = square_size
        
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

        self.clock = pygame.time.Clock()

        self.board = board.Board(self.win, self.squre_size)

        
    def localMultyplayer(self):
        
        def draw():
            self.win.fill(self.bgcolour)
            
            self.board.draw_board()

            pygame.display.update()

        running = True
        while running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    running = False 

            #print(pygame.mouse.get_pos())
            draw()

                       