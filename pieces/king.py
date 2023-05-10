class King:

    def __init__(self, notation, x, y):
        self.x = x
        self.y = y
        self.notation = notation

    def possible_moves(self, board):
        possible_moves = list()

        k_m = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in k_m:
            if 0 <= self.x + i[0] < len(board) and 0 <= self.y + i[1] < len(board):
                if board[self.x + i[0]][self.y + i[1]] is not None and board[self.x + i[0]][self.y + i[1]][1] == self.notation[1]:
                    continue
                else:
                    possible_moves.append([self.x + i[0], self.y + i[1]])

        return possible_moves