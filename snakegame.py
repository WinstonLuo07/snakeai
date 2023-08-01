import pygame as pyg
import numpy
import snake

def displayGame(board, resolution):
    SNAKE = (255, 255, 255) #white
    BACKGROUND = (65, 65, 65) #gray
    APPLE = (255, 0, 0) #red
    
    
    for x in range(len(board)):
        for y in range(0, len(board[x])):
            
            color = BACKGROUND
            if board[x][y] == 1:
                color = SNAKE
            elif board[x][y] == 2:
                color = APPLE

            
            rect = pyg.Rect(x * resolution, y * resolution,resolution, resolution)
            pyg.draw.rect(screen, color, rect)

GRIDX,GRIDY = 16, 16
RESOLUTION = 20

#pygame stuff
pyg.init()
screen = pyg.display.set_mode((GRIDX * RESOLUTION,GRIDY * RESOLUTION))
clock = pyg.time.Clock()
running = True
game = True


snek = snake.snake(GRIDX, GRIDY)
direction = snek.direction
while running:
    

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_w:
                direction = (0, -1)
            elif event.key == pyg.K_s:
                direction = (0, 1)
            elif event.key == pyg.K_d:
                direction = (1, 0)
            elif event.key == pyg.K_a:
                direction = (-1, 0)
            
    screen.fill((65,65,65))
    #graphics display here
    
    if game:
        result = snek.tick(direction)
        displayGame(snek.board, RESOLUTION)
        if result == -1:
            game = False
            print(snek.calculateScore())
    displayGame(snek.board, RESOLUTION)
    
    pyg.display.flip()
    
    clock.tick(10)
pyg.quit()