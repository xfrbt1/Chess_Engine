class Knight:

    def __init__(self, notation, x, y):
        self.x = x
        self.y = y
        self.notation = notation

    # def possible_moves(self, board):
    #     possible_moves = list()
    #
    #     if self.x - 1 >= 0 and self.y - 2 >= 0:
    #         if board[self.x - 1][self.y - 2] is not None and board[self.x - 1][self.y - 2][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x - 1, self.y - 2])
    #
    #     if self.x - 2 >= 0 and self.y - 1 >= 0:
    #         if board[self.x - 2][self.y - 1] is not None and board[self.x - 2][self.y - 1][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x - 2, self.y - 1])
    #
    #     if self.x - 2 >= 0 and self.y + 1 < len(board):
    #         if board[self.x - 2][self.y + 1] is not None and board[self.x - 2][self.y + 1][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x - 2, self.y + 1])
    #
    #     if self.x - 1 >= 0 and self.y + 2 < len(board):
    #         if board[self.x - 1][self.y + 2] is not None and board[self.x - 1][self.y + 2][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x - 1, self.y + 2])
    #
    #     if self.x + 1 < len(board) and self.y + 2 < len(board):
    #         if board[self.x + 1][self.y + 2] is not None and board[self.x + 1][self.y + 2][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x + 1, self.y + 2])
    #
    #     if self.x + 2 < len(board) and self.y + 1 < len(board):
    #         if board[self.x + 2][self.y + 1] is not None and board[self.x + 2][self.y + 1][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x + 2, self.y + 1])
    #
    #     if self.x + 2 < len(board) and self.y - 1 >= 0:
    #         if board[self.x + 2][self.y - 1] is not None and board[self.x + 2][self.y - 1][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x + 2, self.y - 1])
    #
    #     if self.x + 1 < len(board) and self.y - 2 >= 0:
    #         if board[self.x + 1][self.y - 2] is not None and board[self.x + 1][self.y - 2][1] == self.notation[1]:
    #             pass
    #         else:
    #             possible_moves.append([self.x + 1, self.y - 2])
    #
    #     return possible_moves

    def possible_moves(self, board):
        possible_moves = list()

        k_m = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
        for i in k_m:
            if 0 <= self.x + i[0] < len(board) and 0 <= self.y + i[1] < len(board):
                if board[self.x + i[0]][self.y + i[1]] is not None and board[self.x + i[0]][self.y + i[1]][1] == self.notation[1]:
                    continue
                else:
                    possible_moves.append([self.x + i[0], self.y + i[1]])

        return possible_moves