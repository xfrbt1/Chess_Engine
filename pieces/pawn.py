import math


class Pawn:

    def __init__(self, notation, x, y):
        self.x = x
        self.y = y
        self.notation = notation

    def enpassant_w(self, prev, possible_moves):
        print(prev)
        if prev[0] == 'pb':
            if prev[1] == 1 and prev[3] == 3:
                if abs(prev[2] - self.y) == 1:
                    if self.x == 3:
                        possible_moves.append([2, prev[4]])

    def enpassant_b(self, prev, possible_moves):
        print(prev)
        if prev[0] == 'pw':
            if prev[1] == 6 and prev[3] == 4:
                if abs(prev[2] - self.y) == 1:
                    if self.x == 4:
                        possible_moves.append([5, prev[4]])

    def possible_moves(self, x, y, board, move_term, all_moves):
        possible_moves = list()

        if move_term == 1 and self.notation[1] == 'w':
            if x == 0:
                possible_moves.clear()
                return possible_moves
            if board[x - 1][y] is None:
                possible_moves.append([x - 1, y])
            if board[x - 2][y] is None and board[x - 1][y] is None and self.x == 6:
                possible_moves.append([x - 2, y])
            if y != 0 and board[x - 1][y - 1] is not None and board[x - 1][y - 1][1] != 'w':
                possible_moves.append([x - 1, y - 1])
            if y != 7 and board[x - 1][y + 1] is not None and board[x - 1][y + 1][1] != 'w':
                possible_moves.append([x - 1, y + 1])
            if len(all_moves) >= 1:
                self.enpassant_w(all_moves[-1], possible_moves)

        if move_term == 0 and self.notation[1] == 'b':
            if x == 7:
                possible_moves.clear()
                return possible_moves
            if board[x + 1][y] is None:
                possible_moves.append([x + 1, y])
            if self.x == 1 and board[x + 2][y] is None and board[x + 1][y] is None:
                possible_moves.append([x + 2, y])
            if y != 7 and board[x + 1][y + 1] is not None and board[x + 1][y + 1][1] != 'b':
                possible_moves.append([x + 1, y + 1])
            if y != 0 and board[x + 1][y - 1] is not None and board[x + 1][y - 1][1] != 'b':
                possible_moves.append([x + 1, y - 1])
            if len(all_moves) >= 1:
                self.enpassant_b(all_moves[-1], possible_moves)

        return possible_moves
