class Bishop:

    def __init__(self, notation, x, y):
        self.x = x
        self.y = y
        self.notation = notation

    def possible_moves(self, board):
        possible_moves = list()

        '''diagonals'''
        i = self.x - 1
        j = self.y + 1
        while i > -1 and j < len(board):
            if board[i][j] is None:
                possible_moves.append([i, j])
            if board[i][j] is not None:
                if board[i][j][1] != self.notation[1]:
                    possible_moves.append([i, j])
                    break
            if board[i][j] is not None:
                if board[i][j][1] == self.notation[1]:
                    break
            i -= 1
            j += 1

        i = self.x + 1
        j = self.y + 1
        while i < len(board) and j < len(board):
            if board[i][j] is None:
                possible_moves.append([i, j])
            if board[i][j] is not None:
                if board[i][j][1] != self.notation[1]:
                    possible_moves.append([i, j])
                    break
            if board[i][j] is not None:
                if board[i][j][1] == self.notation[1]:
                    break
            i += 1
            j += 1

        i = self.x + 1
        j = self.y - 1
        while i < len(board) and j > -1:
            if board[i][j] is None:
                possible_moves.append([i, j])
            if board[i][j] is not None:
                if board[i][j][1] != self.notation[1]:
                    possible_moves.append([i, j])
                    break
            if board[i][j] is not None:
                if board[i][j][1] == self.notation[1]:
                    break
            i += 1
            j -= 1

        i = self.x - 1
        j = self.y - 1
        while i > -1 and j > -1:
            if board[i][j] is None:
                possible_moves.append([i, j])
            if board[i][j] is not None:
                if board[i][j][1] != self.notation[1]:
                    possible_moves.append([i, j])
                    break
            if board[i][j] is not None:
                if board[i][j][1] == self.notation[1]:
                    break
            i -= 1
            j -= 1

        return possible_moves
