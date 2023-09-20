import pygame
import random

pygame.init()

# Screen setup
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake setup
snake_block = 10
snake_speed = 7

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, 'brown', [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    # Initial position
    x1, y1 = width/2, height/2
    dx, dy = 0, 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            win.fill(white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += dx
        y1 += dy
        win.fill('Cornsilk')
        pygame.draw.rect(win, 'DarkGreen', [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
