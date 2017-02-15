
import numpy as np


class RandomPlayer:
    
    def __init__(self, pid):
        self.id = pid        
        
    def MakeAMove(self, board):
        l = board.GetPossibleMovesForPlayer(self.id)       
        
        if(len(l) == 0):
            return None        
            
        selIndex = np.random.choice(len(l), 1)[0]
        
        return l[selIndex]

#
class GreedyPlayer:
    
    def __init__(self, pid):
        self.id = pid        
        
    def MakeAMove(self, board):
        l = board.GetPossibleMovesForPlayer(self.id)       
        
        if(len(l) == 0):
            return None        
        
        bestMove = None
        maxNum = -1
        for move in l:
            b = board.GetNextBoardAfterMove(move, self.id)
            c = b.GetCount()[self.id - 1] 
            if(c > maxNum):
                maxNum = c
                bestMove = [move]
            elif(c == maxNum):
                bestMove.append(move)
            
        selIndex = np.random.choice(len(bestMove), 1)[0]
        
        return bestMove[selIndex]