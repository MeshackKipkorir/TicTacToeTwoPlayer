board = [' ' for x in range(10)] #board spaces

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

#player one move
def playerOneMove():
    print('****Player One Turn****')
    run = True
    while run:
        move = raw_input('Enter a position you want to play (1 - 9) ')
        move = int(move)
        try:
            if 0 < move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print(' That space is taken, Try another move')
            else:
                print('Enter a number between 1 and 9')
        except:
            print('please enter a number ')
            
 #player two move
def playertwoMove():
    print('****Player Two Turn****')
    run = True
    while run:
        move = raw_input('Enter a position you want to play (1-9) ')
        move = int(move)
        try:
            if 0 < move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('that space is taken. Try another move')
            else:
                print('Enter a number between 1 and 9')
        except:
            print('Please enter a number')


 
def main():
    print('*****Welcome to the game !!!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerOneMove()
            printBoard(board)
        else:
            print('Player Two Won !')
            break

        if not (isWinner(board, 'X')):
            playertwoMove()
            printBoard(board)
        else:
            print('Player One Won')
            break

        if isBoardFull(board):
            print('Tie game !')

#print board
def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')


while True:
    x = raw_input('Do you wanna play again ?(y/n) ')
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('------------------------')
        main()
    else:
        break

            
            
   

   
