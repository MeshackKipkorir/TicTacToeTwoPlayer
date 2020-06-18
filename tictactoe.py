board = [' ' * 10] #board spaces

#insert letter to board
def insertLetter(letter,position):
    board[position] = letter
    return board[position]
   
#check if space if free
def isSpaceFree(position):
    return board[position] == ' '

#check if board is full
def isBoardFull(board):
    if board.count(' ') > 0:
        return False
    else:
        return True
    
    


   
