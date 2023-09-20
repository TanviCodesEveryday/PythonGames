import pygame
import random

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Screen settings
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Tetris blocks
TETROMINOS = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 1],
     [0, 0, 1]],

    [[1, 1, 1, 1]]
]

# Initialize variables
clock = pygame.time.Clock()
current_tetromino = random.choice(TETROMINOS)
current_position = {'x': 3, 'y': 0}
grid = [[0 for _ in range(10)] for _ in range(20)]


def draw_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                pygame.draw.rect(SCREEN, ORANGE, (j * 30, i * 30, 29, 29))


def draw_tetromino(tetromino, position):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] == 1:
                pygame.draw.rect(SCREEN, GREEN, ((position['x'] + j) * 30, (position['y'] + i) * 30, 29, 29))


def rotate_tetromino(tetromino):
    return [[tetromino[y][x]
             for y in range(len(tetromino))]
            for x in range(len(tetromino[0]) - 1, -1, -1)]


def collision(tetromino, position):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] == 1:
                x = position['x'] + j
                y = position['y'] + i
                if x < 0 or x >= 10 or y >= 20 or (y >= 0 and grid[y][x] == 1):
                    return True
    return False


def merge_tetromino(tetromino, position):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] == 1:
                grid[position['y'] + i][position['x'] + j] = 1


def clear_lines():
    lines_to_clear = [i for i, row in enumerate(grid) if all(cell == 1 for cell in row)]
    for i in lines_to_clear:
        del grid[i]
        grid.insert(0, [0 for _ in range(10)])


def main():
    global current_tetromino, current_position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            new_position = {'x': current_position['x'] - 1, 'y': current_position['y']}
            if not collision(current_tetromino, new_position):
                current_position = new_position

        if keys[pygame.K_RIGHT]:
            new_position = {'x': current_position['x'] + 1, 'y': current_position['y']}
            if not collision(current_tetromino, new_position):
                current_position = new_position

        if keys[pygame.K_DOWN]:
            new_position = {'x': current_position['x'], 'y': current_position['y'] + 1}
            if not collision(current_tetromino, new_position):
                current_position = new_position

        if keys[pygame.K_UP]:
            rotated = rotate_tetromino(current_tetromino)
            if not collision(rotated, current_position):
                current_tetromino = rotated

        SCREEN.fill(BLACK)

        new_position = {'x': current_position['x'], 'y': current_position['y'] + 1}
        if not collision(current_tetromino, new_position):
            current_position = new_position
        else:
            merge_tetromino(current_tetromino, current_position)
            clear_lines()
            current_tetromino = random.choice(TETROMINOS)
            current_position = {'x': 3, 'y': 0}
            if collision(current_tetromino, current_position):
                print("Game Over!")
                pygame.quit()
                quit()

        draw_grid()
        draw_tetromino(current_tetromino, current_position)

        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
