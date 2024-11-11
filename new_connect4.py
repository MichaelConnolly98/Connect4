import numpy as np
import pygame 
import sys
import math
# from itertools import cycle


pygame.init()

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 -5)
screen = pygame.display.set_mode(size)
game_over = False
turn = 0
myfont = pygame.font.SysFont('helveticaneue', 75)

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)



class game_setup:
    def __init__(self, row_count=ROW_COUNT, col_count=COLUMN_COUNT):
        self.row_count = row_count
        self.col_count = col_count
        self.create_board()
        self.drop_piece()
        self.is_valid_location()
        self.get_next_open_row()
        self.print_board()

    def create_board(self):
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board
    
    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[ROW_COUNT-1][col] == 0
    
    def get_next_open_row(self, board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r
            
    def print_board(self, board):
        print(np.flip(board,0))

    def winning_move(self, board, piece):
        # check all horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
                
        # check all veritical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True
                
        # check for positively sloped diagonals
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True
        
        # check for negatively sloped diagonals
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
                
class game_board:
    def __init__(self, game):
        self._game = game
        self.draw_board()
    

    def draw_board(self, board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):        
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

        pygame.display.update()

    def play(self):
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))

                    # ask for Player 1 Input
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if self._game.is_valid_location(board, col):
                            row = self._game.get_next_open_row(board, col)
                            self._game.drop_piece(board, row, col, 1)

                            if self._game.winning_move(board, 1):
                                label = myfont.render("Player 1 Wins!", 1 , RED)
                                screen.blit(label, (100,10))
                                game_over = True
                    
                    # ask for Player 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx/SQUARESIZE))

                        if self._game.is_valid_location(board, col):
                            row = self._game.get_next_open_row(board, col)
                            self._game.drop_piece(board, row, col, 2)

                            if self._game.winning_move(board, 1):
                                label = myfont.render("Player 2 Wins!", 1 , RED)
                                screen.blit(label, (100,10))
                                game_over = True
                
                self.draw_board(board)
                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)

def main():
    game = game_setup()
    board = game_board(game)
    board.play()

if __name__ == "__main__":
    main()