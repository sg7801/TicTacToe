import math
import random
import pygame
from spot import Spot

def best(board, comp, result):
    all_empty = True
    bestScore = -math.inf
    row, column = None, None
    
    for i in range(3):
        for j in range(3):
            if board[i][j].isEmpty():
                pass
            else:
                all_empty = False
                break
                
    if all_empty:
        return random.choice([(0,0), (0,2), (2,0), (2,2)])
    
    for i in range(3):
        for j in range(3):
            if board[i][j].isEmpty():
                board[i][j].val = comp
                score = minimax(board, 0, False, comp, result) 
                board[i][j].val = 0
                if score > bestScore:
                    bestScore = score
                    row, column = i, j
    return row, column

def minimax(board, depth, maximizing, computer, result):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if result() != None:
        score = result()*computer
        return score
    if maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j].isEmpty():
                    board[i][j].val = computer
                    score = minimax(board, depth+1, not maximizing, computer, result)
                    board[i][j].val = 0
                    best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j].isEmpty():
                    board[i][j].val = -computer
                    score = minimax(board, depth+1, not maximizing, computer, result)
                    board[i][j].val = 0
                    best = max(score, best)
        return best
            