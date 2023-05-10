H = 480
dim = 8

sq_size = H // dim

fps = 60

caption = 'CHESS'

# self.board = [
#     [None, None, None, None, None, None, None, None, ],  # 8 - i - 0
#     [None, None, None, None, None, None, None, None, ],  # 7 - i - 1
#     [None, None, None, None, None, None, None, None, ],  # 6 - i - 2
#     [None, None, None, None, None, None, None, None, ],  # 5 - i - 3
#     [None, None, None, None, None, None, None, None, ],  # 4 - i - 4
#     [None, None, None, None, None, None, None, None, ],  # 3 - i - 5
#     [None, None, None, None, None, None, None, None, ],  # 2 - i - 6
#     [None, None, None, None, None, None, None, None, ],  # 1 - i - 7
#     # a-j-0 b-j-1 c-j-2 d-j-3 e-j-4 f-j-5 g-j-6 h-j-7
# ]

# self.board = [
#     ['rb', 'nb', 'bb', 'qb', 'kb', 'bb', 'nb', 'rb', ],  # 8 - i - 0
#     ['pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb', ],  # 7 - i - 1
#     [None, None, None, None, None, None, None, None, ],  # 6 - i - 2
#     [None, None, None, None, None, None, None, None, ],  # 5 - i - 3
#     [None, None, None, None, None, None, None, None, ],  # 4 - i - 4
#     [None, None, None, None, None, None, None, None, ],  # 3 - i - 5
#     ['pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', ],  # 2 - i - 6
#     ['rw', 'nw', 'bw', 'qw', 'kw', 'bw', 'nw', 'rw', ],  # 1 - i - 7
#     # a-j-0 b-j-1 c-j-2 d-j-3 e-j-4 f-j-5 g-j-6 h-j-7
# ]