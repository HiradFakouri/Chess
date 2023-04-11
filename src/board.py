import pygame

class Board:

    def __init__(self, screen, square_size):
        self.square_size = square_size
        self.screen = screen
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.board = [[], [], [], [], [], [], [], []] 

    def draw_board(self):
        for row in range(8):
            for column in range(8):
                x = column * self.square_size
                y = row * self.square_size

                if (row + column) % 2 == 0:
                    color = self.white
                else:
                    color = self.black
                
                self.board[row].append({"pos": (row, column), "color": color, "piece_on_top": 0})
                pygame.draw.rect(self.screen, color, [x, y, self.square_size, self.square_size])
                
