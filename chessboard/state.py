import pygame
from config import *
from pieces import *

from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.king import King


class CurrentGameState:

    def __init__(self):

        self.board = [
            [None, None, None, None, None, None, None, None, ],  # 8 - i - 0
            [None, None, None, None, None, None, None, None, ],  # 7 - i - 1
            [None, None, None, None, None, None, None, None, ],  # 6 - i - 2
            [None, None, None, None, None, None, None, None, ],  # 5 - i - 3
            [None, None, None, None, None, None, None, None, ],  # 4 - i - 4
            [None, None, None, None, None, None, None, None, ],  # 3 - i - 5
            [None, None, None, None, None, None, None, None, ],  # 2 - i - 6
            ['nw', None, None, None, None, None, None, None, ],  # 1 - i - 7
            # a-j-0 b-j-1 c-j-2 d-j-3 e-j-4 f-j-5 g-j-6 h-j-7
        ]

        self.valid_moves = []
        self.all_moves = []
        self.move_term = True
        self.pawn_to_queen = ['qb', 'qw']
        self.chosen_figure = []

    def change_move_term(self):
        if self.move_term:
            self.move_term = False
        else:
            self.move_term = True

    def print_board_coordinates(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                print(f"[{i}][{j}]|{self.board[i][j]}|", end=' ')
            print("\n")

    def draw_board(self, screen):
        colors = [(200, 200, 200), (150, 150, 150)]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                color = colors[((i + j) % 2)]
                pygame.draw.rect(screen, pygame.Color(color), pygame.Rect(j * sq_size, i * sq_size, sq_size, sq_size))

    def draw_chosen_figure(self, screen):
        if len(self.chosen_figure) == 2:
            pygame.draw.rect(screen, pygame.Color((255, 147, 203)),
                             pygame.Rect(self.chosen_figure[1] * sq_size + 5, self.chosen_figure[0] * sq_size + 5,
                                         sq_size - 10, sq_size - 10))

    def draw_valid_moves(self, screen):
        for i in self.valid_moves:
            pygame.draw.rect(screen, pygame.Color((255, 147, 203)),
                             pygame.Rect(i[1] * sq_size + 5, i[0] * sq_size + 5, sq_size - 10, sq_size - 10))

    def draw_figures(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] is not None:
                    screen.blit(pygame.image.load(
                        f"/Users/aleksej/Desktop/python/Chess_Engine/pieces/img/{self.board[i][j]}.png"),
                        pygame.Rect(j * sq_size, i * sq_size, sq_size, sq_size))

    def draw_prev_moves(self, screen):
        if len(self.all_moves) > 0:
            for i in range(len(self.all_moves)):
                pygame.draw.rect(screen, pygame.Color((0, 255, 10)),
                                 pygame.Rect(self.all_moves[i][2] * sq_size + 5, self.all_moves[i][1] * sq_size + 5, sq_size - 10, sq_size - 10))

    def draw_current_game_state(self, screen):
        self.draw_board(screen)

        self.draw_chosen_figure(screen)

        self.draw_valid_moves(screen)

        self.draw_figures(screen)

        self.draw_prev_moves(screen)

    def check_for_pieces(self, x, y):
        if self.board[x][y] is not None:
            print(self.board[x][y], x, y)
            return True

    def get_valid_moves(self, x, y):
        notation = self.board[x][y]

        if (notation[1] == 'w' and self.move_term == 1) or (notation[1] == 'b' and self.move_term == 0):

            if notation[0] == 'p':
                pawn = Pawn(notation, x, y)
                self.valid_moves = pawn.possible_moves(x, y, self.board, self.move_term, self.all_moves)

            if notation[0] == 'q':
                queen = Queen(notation, x, y)
                self.valid_moves = queen.possible_moves(self.board)

            if notation[0] == 'b':
                bishop = Bishop(notation, x, y)
                self.valid_moves = bishop.possible_moves(self.board)

            if notation[0] == 'r':
                rook = Rook(notation, x, y)
                self.valid_moves = rook.possible_moves(self.board)

            if notation[0] == 'n':
                knight = Knight(notation, x, y)
                self.valid_moves = knight.possible_moves(self.board)

            if notation[0] == 'k':
                king = King(notation, x, y)
                self.valid_moves = king.possible_moves(self.board)

    def make_move(self, x_c, y_c, x, y):
        notation = self.board[x_c][y_c]

        # if len(self.all_moves) > 1 and self.board[x_c][y_c] == 'pw' and self.all_moves[-1][3] == 3 and self.all_moves[-1][1] == 1 and (y_c == self.all_moves[-1][4] + 1 or y_c == self.all_moves[-1][4] - 1) and x == 3:
        #     capture_figure = self.all_moves[-1][0]
        #     self.board[self.all_moves[-1][3]][self.all_moves[-1][4]] = None
        #     self.board[x][y] = notation
        #     self.board[x_c][y_c] = None
        #     print('en passant w')
        #     self.valid_moves.clear()
        #     self.all_moves.append([notation, x_c, y_c, x, y, capture_figure, 'en_passant_w'])
        #
        # elif self.board[x][y] == 'pb' and self.all_moves[-1][3] == 4 and self.all_moves[-1][1] == 6 and (
        #         y_c == self.all_moves[-1][4] + 1 or y_c == self.all_moves[-1][4] - 1):
        #     capture_figure = self.all_moves[-1][0]
        #     self.board[self.all_moves[-1][3]][self.all_moves[-1][4]] = None
        #     self.board[x][y] = notation
        #     self.board[x_c][y_c] = None
        #     print('en passant b')
        #     self.valid_moves.clear()
        #     self.all_moves.append([notation, x_c, y_c, x, y, capture_figure, 'en_passant_b'])

        if self.board[x][y] is not None:
            if notation[0] == 'p' and (x == 0 or x == 7):
                notation = 'q' + self.board[x_c][y_c][1]
            capture_figure = self.board[x][y]
            self.board[x][y] = notation
            self.board[x_c][y_c] = None
            self.valid_moves.clear()
            self.all_moves.append([notation, x_c, y_c, x, y, capture_figure, 'capture'])

        else:
            if notation[0] == 'p' and (x == 0 or x == 7):
                notation = 'q' + self.board[x_c][y_c][1]
            self.board[x][y] = notation
            self.board[x_c][y_c] = None
            self.valid_moves.clear()
            self.all_moves.append([notation, x_c, y_c, x, y, None, 'move'])

        # self.change_move_term()
        print(self.all_moves)
