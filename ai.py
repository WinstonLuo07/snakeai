import pygame as pyg
import numpy
import random
import network
import snake

def playAIO(moveLimit, generationSize):
    bestNn = network.NeuralNet((GRIDX*GRIDY, 4))
    bestSnake = snake.snake(GRIDX, GRIDY)
    for game in range(0, generationSize):
        
        nn =  network.NeuralNet((GRIDX*GRIDY, 20, 12, 4))
        snek = snake.snake(GRIDX, GRIDY)
        
        
        direction = (0, 1)
        move = moveLimit
        while snek.tick(direction) != -1 and move > 0:
            decision = nn.makeDecision(snek.board.flatten())
            direction = snek.finddirection(snek.direction, parseNN(decision))
            move -= 1
        if snek.calculateScore() > bestSnake.calculateScore():
            bestNn = nn
            bestSnake = snek
    return bestNn
def playAI(moveLimit, generationSize, neuralnetwork, mrate, mchance):
    bestNn = network.NeuralNet((GRIDX*GRIDY, 4))
    bestSnake = snake.snake(GRIDX, GRIDY)
    for game in range(0, generationSize):
        nn =  neuralnetwork.createOffSpring(mrate, mchance)
        snek = snake.snake(GRIDX, GRIDY)
        # print("game " + str(game))
        
        direction = (0, 1)
        move = moveLimit
        while snek.tick(direction) != -1 and move > 0:
            decision = nn.makeDecision(snek.board.flatten())
            direction = snek.finddirection(snek.direction, parseNN(decision))
            move -= 1
            
            displayGame(snek.board, RESOLUTION)
            pyg.display.flip()
            clock.tick(50)
            
            
        if snek.calculateScore() > bestSnake.calculateScore():
            bestNn = nn
            bestSnake = snek
    print("Best Fit: " + str(bestSnake.calculateScore()))
    return bestNn

def parseNN(decision):
    direction = (0, 0)
    if decision == 0:
        direction = (0, 1)
    elif decision == 1:
        direction = (0, -1)
    elif decision == 2:
        direction = (1, 0)
    elif decision == 3:
        direction = (-1, 0)
    return direction

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


GRIDX,GRIDY = 10, 10
RESOLUTION = 40

#pygame stuff
pyg.init()
screen = pyg.display.set_mode((GRIDX * RESOLUTION,GRIDY * RESOLUTION))
clock = pyg.time.Clock()
running = True
game = True

#generation stuff
genSize = 500
moveLimit = 250
generations = 100
diversity = 0.4
mutationChance = 0.2


bestAI = playAIO(moveLimit=moveLimit,generationSize=genSize)
for generation in range(0,generations):
    print("generation " + str(generation))
    bestAI = playAI(moveLimit=moveLimit,generationSize=genSize, neuralnetwork=bestAI, mrate=diversity, mchance=mutationChance)


snek = snake.snake(GRIDX, GRIDY)
direction = snek.direction
while running:
    

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
            
    screen.fill((65,65,65))
    #graphics display here
    
    if snek.tick(direction) != -1:
        decision = bestAI.makeDecision(snek.board.flatten())
        direction = snek.finddirection(snek.direction, parseNN(decision))
    else:
        print(snek.calculateScore())
        
    
    displayGame(snek.board, RESOLUTION)
    pyg.display.flip()
    
    clock.tick(10)
pyg.quit()