
import numpy as np

class Board:
    
    def __init__(self):        
        self._board = np.zeros([8, 8])
        self._SetPlaces([[3,3],[4,4]], 1)
        self._SetPlaces([[3,4],[4,3]], 2)

    def _SetPlaces(self, places, value):
        for i,j in places:
            self._board[i][j] = value

    def ShowBoard(self):
        print(self._board)    
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
    def GetCount(self):
        c1 = np.sum(np.equal(self._board, 1))
        c2 = np.sum(np.equal(self._board, 2))
        return [c1, c2]
        
    def GetPossibleMovesForPlayer(self, player):
        positionList = []
        
        for i in range(8):
            for j in range(8):    
                if(self._board[i][j] != 0):
                    continue
                
                if(                   
                   self._SearchRight([i,j], player) or
                   self._SearchLeft([i,j], player) or
                   self._SearchAbove([i,j], player) or
                   self._SearchBelow([i,j], player) or
                   self._SearchDiagonalTopRight([i,j], player) or
                   self._SearchDiagonalBottomRight([i,j], player) or
                   self._SearchDiagonalTopLeft([i,j], player) or
                   self._SearchDiagonalBottomLeft([i,j], player)                   
                   ):
                    positionList.append([i,j])
                    
        return positionList        
        
    def GetNextBoardAfterMove(self, position, player):
                
        if(not position):
            b = Board()
            b._board = self._board.copy()  
            return b
             
        tmpBoard = self._board.copy()
        
        i,j = position
        tmpBoard[i][j] = player
        opponent = 3 - player 
        
        if(self._SearchRight(position, player)):
            k = j+1
            while(tmpBoard[i][k] == opponent):
                tmpBoard[i][k] = player
                k += 1

        if(self._SearchLeft(position, player)):
            k = j-1
            while(tmpBoard[i][k] == opponent):
                tmpBoard[i][k] = player
                k -= 1
                
        if(self._SearchAbove(position, player)):
            k = i-1
            while(tmpBoard[k][j] == opponent):
                tmpBoard[k][j] = player
                k -= 1
                
        if(self._SearchBelow(position, player)):
            k = i+1
            while(tmpBoard[k][j] == opponent):
                tmpBoard[k][j] = player
                k += 1
        
        if(self._SearchDiagonalTopLeft(position, player)):            
            k = 1            
            while(tmpBoard[i-k][j-k] == opponent):
                tmpBoard[i-k][j-k] = player
                k += 1
            
        if(self._SearchDiagonalTopRight(position, player)):            
            k = 1            
            while(tmpBoard[i-k][j+k] == opponent):
                tmpBoard[i-k][j+k] = player
                k += 1
                
        if(self._SearchDiagonalBottomRight(position, player)):            
            k = 1            
            while(tmpBoard[i+k][j+k] == opponent):
                tmpBoard[i+k][j+k] = player
                k += 1
                           
        if(self._SearchDiagonalBottomLeft(position, player)):            
            k = 1            
            while(tmpBoard[i+k][j-k] == opponent):
                tmpBoard[i+k][j-k] = player
                k += 1   
        
        b = Board()
        b._board = tmpBoard
        return b       
                
                    
    def _SearchRight(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(j >= 6):
             return False
             
        if(self._board[i][j+1] == opponent):
            for k in range(j+2, 8):
                if(self._board[i][k] == 0):
                    return False
                if(self._board[i][k] == player):
                    return True  
                    
        return False            
        
    def _SearchLeft(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(j <= 1):
             return False
             
        if(self._board[i][j-1] == opponent):
            for k in range(j-2, -1, -1):
                if(self._board[i][k] == 0):
                    return False
                if(self._board[i][k] == player):
                    return True  
                    
        return False
         
    def _SearchAbove(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(i <= 1):
             return False
             
        if(self._board[i-1][j] == opponent):
            for k in range(i-2, -1, -1):
                if(self._board[k][j] == 0):
                    return False 
                if(self._board[k][j] == player):
                    return True  
                    
        return False
        
        
    def _SearchBelow(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(i >= 6):
             return False
             
        if(self._board[i+1][j] == opponent):
            for k in range(i+2, 8):
                if(self._board[k][j] == 0):
                    return False                    
                if(self._board[k][j] == player):
                    return True  
                    
        return False
    
    def _SearchDiagonalTopRight(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(i <= 1 or j >= 6):
             return False
        
        num = np.min([i-2, 6-j])
        if(self._board[i-1][j+1] == opponent):
            for k in range(2, 2+num):
                if(self._board[i-k][j+k] == 0):
                    return False                    
                if(self._board[i-k][j+k] == player):
                    return True  
                    
        return False

    def _SearchDiagonalTopLeft(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(i <= 1 or j <= 1):
             return False
        
        num = np.min([i-2, j-2])
        if(self._board[i-1][j-1] == opponent):
            for k in range(2, 2+num):
                if(self._board[i-k][j-k] == 0):
                    return False
                if(self._board[i-k][j-k] == player):
                    return True  
                    
        return False
    
    def _SearchDiagonalBottomRight(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(i >= 6 or j >= 6):
             return False
        
        num = np.min([6-i, 6-j])
        if(self._board[i+1][j+1] == opponent):
            for k in range(2, 2+num):
                if(self._board[i+k][j+k] == 0):
                    return False
                if(self._board[i+k][j+k] == player):
                    return True  
                    
        return False

    def _SearchDiagonalBottomLeft(self, position, player):
        opponent = 3 - player         
        i,j = position         
        if(i >= 6 or j <= 1):
             return False
        
        num = np.min([ 6-i, j-2])
        if(self._board[i+1][j-1] == opponent):
            for k in range(2, 2+num):
                if(self._board[i+k][j-k] == 0):
                    return False
                if(self._board[i+k][j-k] == player):
                    return True  
                    
        return False


                