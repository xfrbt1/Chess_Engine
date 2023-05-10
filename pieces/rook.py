class Rook:

    def __init__(self, notation, x, y):
        self.x = x
        self.y = y
        self.notation = notation

    def possible_moves(self, board):
        possible_moves = list()

        '''horizontal and vertical'''
        for i in (range(self.x + 1, len(board))):

            if board[i][self.y] is None:
                possible_moves.append([i, self.y])

            if board[i][self.y] is not None:
                if board[i][self.y][1] != self.notation[1]:
                    possible_moves.append([i, self.y])
                    break

            if board[i][self.y] is not None:
                if board[i][self.y][1] == self.notation[1]:
                    break

        for i in range(self.x - 1, -1, -1):
            if board[i][self.y] is None:
                possible_moves.append([i, self.y])

            if board[i][self.y] is not None:
                if board[i][self.y][1] != self.notation[1]:
                    possible_moves.append([i, self.y])
                    break

            if board[i][self.y] is not None:
                if board[i][self.y][1] == self.notation[1]:
                    break

        for i in (range(self.y + 1, len(board))):

            if board[self.x][i] is None:
                possible_moves.append([self.x, i])

            if board[self.x][i] is not None:
                if board[self.x][i][1] != self.notation[1]:
                    possible_moves.append([self.x, i])
                    break

            if board[self.x][i] is not None:
                if board[self.x][i][1] == self.notation[1]:
                    break

        for i in (range(self.y - 1, -1, -1)):

            if board[self.x][i] is None:
                possible_moves.append([self.x, i])

            if board[self.x][i] is not None:
                if board[self.x][i][1] != self.notation[1]:
                    possible_moves.append([self.x, i])
                    break

            if board[self.x][i] is not None:
                if board[self.x][i][1] == self.notation[1]:
                    break

        return possible_moves
