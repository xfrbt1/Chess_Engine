import pygame
import sys

from config import *
from chessboard.state import CurrentGameState


def main():
    pygame.init()
    screen = pygame.display.set_mode((H, H))
    pygame.display.set_caption(caption)
    clock = pygame.time.Clock()
    gf = CurrentGameState()
    # gf.draw_current_game_state(screen)
    # gf.print_board_coordinates()
    x_c = None
    y_c = None

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                coordinates = pygame.mouse.get_pos()
                x, y = coordinates[1] // sq_size, coordinates[0] // sq_size
                if len(gf.valid_moves) != 0 and [x, y] in gf.valid_moves:
                    gf.make_move(x_c, y_c, x, y)
                    gf.chosen_figure.clear()
                    break

                if gf.check_for_pieces(x, y):
                    gf.valid_moves.clear()
                    x_c = x
                    y_c = y
                    gf.get_valid_moves(x, y)
                    gf.chosen_figure = [x, y]

                else:
                    gf.valid_moves.clear()
                    x_c = None
                    y_c = None
                    print("none at ", x, y)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('space')

        clock.tick(fps)
        pygame.display.flip()
        gf.draw_current_game_state(screen)


if __name__ == "__main__":
    main()
