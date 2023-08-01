import pygame as pyg
import numpy
import random
import network
import math

class snake:
    
    
    def __init__(self, GRIDX, GRIDY):
        self.board = numpy.zeros((GRIDX,GRIDY))
        self.snake = [[int(GRIDX / 2), int(GRIDY / 2)],[int(GRIDX / 2 - 1), int(GRIDY / 2)],[int(GRIDX / 2 - 2), int(GRIDY / 2)]]
        self.direction = (1, 0)
        self.apple = False
        self.alive = 0
    

    def spawnApple(self):
        spawned = False
        while not spawned:
            randx = random.randint(0, len(self.board) - 1)
            randy = random.randint(0, len(self.board[0]) - 1)
            
            good = True
            for segment in self.snake:
                if segment[0] == randx and segment[1] == randy:
                    good = False
                
            if good:
                spawned = True
                self.board[randx][randy] = 2
                self.apple = True


    def tick(self, direction):
        self.direction = self.finddirection(self.direction, newdirection=direction)
        
        self.alive += 1
        
        if not self.apple: self.spawnApple()
        
        # (0, 1) down
        # (0, -1) up
        # (1, 0) right
        # (-1, 0) left
        # print(direction)
        if self.direction != [0, 0]:
            head = [numpy.clip(self.snake[0][0] + self.direction[0], 0, len(self.board) - 1), numpy.clip(self.snake[0][1] + self.direction[1], 0, len(self.board[0]) - 1)]
            tail = self.snake[len(self.snake) - 1]
            
            eat = False
            
            if self.board[head[0]][head[1]] == 2:
                eat = True
            if self.board[head[0]][head[1]] == 1:
                #death
                if tail[0] != head[0] or tail[1] != head[1]:
                    return -1
            
            self.board[tail[0],tail[1]] = 0
            self.board[head[0]][head[1]] = 1
            # print(snake)
            
            self.snake.insert(0, head)
            if eat:
                self.apple = False
            else:
                self.snake.remove(tail)
                
    def calculateScore(self):
        apples = len(self.snake) - 3
        
        
        # return len(self.snake) *5* len(self.snake) + self.alive -45
        return self.alive + (math.pow(2, apples) + math.pow(apples, 2.1) * 500) - (math.pow(apples,2.1) * math.pow(0.25 * self.alive, 1.3))

    def finddirection(self, direction, newdirection):
        if direction == (0, 1):
            if newdirection == (0, -1):
                return direction
        if direction == (0, -1):
            if newdirection == (0, 1):
                return direction
        if direction == (1, 0):
            if newdirection == (-1, 0):
                return direction
        if direction == (-1, 0):
            if newdirection == (1, 0):
                return direction
        return newdirection
    # def displayGame(board, resolution):
    #     SNAKE = (255, 255, 255) #white
    #     BACKGROUND = (65, 65, 65) #gray
    #     APPLE = (255, 0, 0) #red
        
        
    #     for x in range(len(board)):
    #         for y in range(0, len(board[x])):
                
    #             color = BACKGROUND
    #             if board[x][y] == 1:
    #                 color = SNAKE
    #             elif board[x][y] == 2:
    #                 color = APPLE

                
    #             rect = pyg.Rect(x * resolution, y * resolution,resolution, resolution)
    #             pyg.draw.rect(screen, color, rect)



    # GRIDX,GRIDY = 16, 16
    # RESOLUTION = 20



# pyg.init()
# screen = pyg.display.set_mode((GRIDX * RESOLUTION,GRIDY * RESOLUTION))
# clock = pyg.time.Clock()
# running = True
# game = True
# alive = 0


# while running:
    

#     for event in pyg.event.get():
#         if event.type == pyg.QUIT:
#             running = False
#         if event.type == pyg.KEYDOWN:
#             if event.key == pyg.K_w:
#                 direction = finddirection(direction, (0, -1))
#             elif event.key == pyg.K_s:
#                 direction = finddirection(direction, (0, 1))
#             elif event.key == pyg.K_d:
#                 direction = finddirection(direction, (1, 0))
#             elif event.key == pyg.K_a:
#                 direction = finddirection(direction, (-1, 0))
            
#     screen.fill((65,65,65))
#     #graphics display here
    
#     if game:
#         result = tick(snake, board, direction)
#         if result == -1:
#             game = False

#     score = alive + len(snake) * len(snake) * 5
    
#     print(score)
#     displayGame(board, RESOLUTION)
    
#     pyg.display.flip()
    
#     clock.tick(10)
# pyg.quit()

