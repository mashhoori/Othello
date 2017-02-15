from Board import Board


class Othello:
    
    def __init__(self, players):        
        self.board = Board()
        self.players = players
                        
    def StartGame(self, startByFirst = True, showBoard = False):
        
        players = [0, 1]
        if(not startByFirst):
            players.reverse()         
        
        noMoveLeft = 0
        move = 0
        while(move < 60 and noMoveLeft < 2):            
            for p in players:
                position = self.players[p].MakeAMove(self.board)
                self.board = self.board.GetNextBoardAfterMove(position, p+1)                       
                if(showBoard):
                    self.board.ShowBoard()
                
                if(position): 
                    move += 1
                    noMoveLeft = 0
                else: 
                    noMoveLeft += 1
                    
                if(move == 60 or noMoveLeft == 2):   
                    break
            


    
    
    
    
       
