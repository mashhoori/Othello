# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 01:38:39 2017

@author: a.mashhoori
"""
from timeit import default_timer as timer
from joblib import Parallel, delayed
import multiprocessing
import  numpy as np
from Othello import Othello
from Players import RandomPlayer, GreedyPlayer


def Play(i, players):    
    oth = Othello(players)
    oth.StartGame( startByFirst = bool(i%2) )            
    result = oth.board.GetCount()
    if(result[0] > result[1]): return 1
    elif(result[0] < result[1]): return -1
    else: return 0
        
##############################################################
if __name__ == '__main__':    
    numGames = 10
    start = timer()

    players = [GreedyPlayer(1), RandomPlayer(2)]
    
##  Multi-Process Version  
##  This version can only be run from command promt
##
    num_cores = multiprocessing.cpu_count() 
    results = Parallel(n_jobs=num_cores)(delayed(Play)(i, players) for i in range(numGames))
    results = np.array(results)
###############################################################

##    Single-Process Version    
#    results = [0] * numGames
#    for i in range( numGames):        
#        results[i] = Play(i, players)      
              
###############################################################
    
    print('-------------------------')
    print('Win for player 1: %.2f' %(np.equal(results, 1).sum() / numGames))
    print('Win for player 2: %.2f' %(np.equal(results, -1).sum() / numGames))
    print('Draw            : %.2f' %(np.equal(results, 0).sum() / numGames))
    print('-------------------------')
    end = timer()
    print('Time elapsed    : %.2f' %(end - start))            
    print('========================')
    