import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
ROW_COUNT = 6
COL_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COL_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
RADIUS = int(SQUARE_SIZE / 2 - 5)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize board
board = np.zeros((ROW_COUNT, COL_COUNT))

# Initialize screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


def check_winner(board, piece):
    # Check horizontal
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check diagonals (positive slope)
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check diagonals (negative slope)
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


# Main loop
game_over = False
turn = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // SQUARE_SIZE

            for r in range(ROW_COUNT):
                if board[r][col] == 0:
                    row = r
                    break
            else:
                continue

            board[row][col] = turn % 2 + 1

            draw_board(board)

            if check_winner(board, turn % 2 + 1):
                print(f"PLAYER {turn % 2 + 1} WINS!")
                game_over = True

            turn += 1
