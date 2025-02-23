#chessboard={'1h':'bking','6c':'wqueen','2g':'bbishop','5h':'bbqueen','3e':'wking'}

def isValidChessBoard():
    '''chess board problem from Automate the boring stuff chapter 5'''
    colors = ('b','w')
    pieces = ('rook','queen','king','bishop','pawn','knight')
    vaxis = ('1','2','3','4','5','6','7','8')
    haxis = ('a','b','c','d','e','f','g')

    def boardBuild(letter,number):
        board=[]
        for i in letter:
            for j in number:
                board.append(str(i)+str(j))
                
        return board
    
    
    theBoard = boardBuild(haxis,vaxis)
    #theBoard = {'a1':'','a2':'','a3':'','a4':'','a5':'','a6':'','a7':'','a8':'','b1':'','b2':''}
    #print('the board is '+str(theBoard))
    return theBoard

print(isValidChessBoard())
