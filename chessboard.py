#chessboard={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bbqueen','3e':'wking'}
import pprint


def isValidChessBoard():
    '''chess board problem from Automate the boring stuff chapter 5'''
    colors = ('b','w')
    pieces = ('rook','queen','king','bishop','pawn','knight')
    vaxis = ('1','2','3','4','5','6','7','8')
    haxis = ('a','b','c','d','e','f','g','h')

    def boardBuild(letter,number):
        #build board with number_letter notation and set to empty initial states
        gridList=[]
        board={}
        for i in number:
            for j in letter:
                gridList.append(str(j)+str(i))

        for t in gridList:
            board.setdefault(t,'')    
        
        #print(board) #used for validation
        return board

    
    
    theBoard = boardBuild(vaxis,haxis)
    
    
    return theBoard

pprint.pprint(isValidChessBoard())
