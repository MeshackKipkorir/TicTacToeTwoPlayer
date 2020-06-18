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
    
#check for winner,checks for rows,diagonals,columns if they have the same letter
def isWinner(board,letter):
    return ((board[1] == board[2] == board[3] == letter) or
            (board[4] == board[5] == board[6] == letter) or
            (board[7] == board[8] == board[9] == letter) or
            (board[1] == board[4] == board[7] == letter) or
            (board[2] == board[5] == board[8] == letter) or
            (board[3] == board[6] == board[9] == letter) or
            (board[1] == board[5] == board[9] == letter) or
            (board[3] == board[5] == board[7] == letter))
    


   
