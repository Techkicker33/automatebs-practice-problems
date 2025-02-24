#chessboard={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bbqueen','3e':'wking'}
'''Chess Dictionary Validator

In this chapter, we used the dictionary value 
{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. 
Write a function named isValidChessBoard() that takes a dictionary argument 
and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. 
Each player can only have at most 16 pieces, at most 8 pawns, 
and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. 
The piece names begin with either a 'w' or 'b' to represent white or black, 
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
This function should detect when a bug has resulted in an improper chess board.'''

import pprint


def isValidChessBoard():
    '''chess board problem from Automate the boring stuff chapter 5'''
    colors = ('b','w')
    pieces = ('rook','queen','king','bishop','pawn','knight')
    vaxis = ('1','2','3','4','5','6','7','8')
    haxis = ('a','b','c','d','e','f','g','h')
    maxPieceCount = 16
    


    def boardBuild(letter,number):
        #build board with number_letter notation and set to empty initial states.  
        # This avoids manually typing the full list
        gridList=[]
        board={}
        for i in number:
            for j in letter:
                gridList.append(str(j)+str(i))

        for t in gridList:
            board.setdefault(t,'')     
        
        return board

        
    theBoard = boardBuild(vaxis,haxis) #call board build function and pass the axis values
    
    if 'bking' or 'wking' in theBoard:
        'print no king is dead'
    elif 'bking' and 'wking' not in theBoard:
        print('Both kings are dead')
        
    
    
    
    return theBoard #pass the board back up to the main level

pprint.pprint(isValidChessBoard()) #print the board in its current state
