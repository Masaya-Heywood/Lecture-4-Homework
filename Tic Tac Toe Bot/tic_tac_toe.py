import turtle
import random

screen_up = False

def go_tic_tac_toe_turn(player,rows,AI_Turn,firstTurn,secondTurn):
    row = False
    col = False
    done = False
    playerMark = 'X'
    bestMoves = [(0,0), (0,2), (1,1), (2,0), (2,2)]
    
    if AI_Turn != True:
        print('Rows are numbered 1 to 3 from top to botton.')
        print('Columns are numbered 1 to 3 from left to right.')
        
    
    
    if AI_Turn == True:
        if firstTurn == True:
            moveSelector = random.randint(0,len(bestMoves)-1)
        
            row_list = rows[bestMoves[moveSelector][0]]
            if row_list[bestMoves[moveSelector][1]] == '_':
                row_list[bestMoves[moveSelector][1]] = player
        elif secondTurn == True:
            row_list = rows[[2][0]]
            if rows[1][1] == '_':
                rows[1][1] = player
            else:
                while not done:
                    moveSelector = random.randint(0,len(bestMoves)-1)
        
                    row_list = rows[bestMoves[moveSelector][0]]
                    if row_list[bestMoves[moveSelector][1]] == '_':
                        row_list[bestMoves[moveSelector][1]] = player
                        done = True
                        
        elif firstTurn != True and secondTurn != True:            
            #examine the board-            
            examinedBoard = []
            for row in range(0,len(rows)):
                rowSlice = [None] * len(rows)
                #print(rowSlice)
                
                for col in range(0,len(rows)):
                    if rows[row][col] == playerMark:
                        rowSlice[col] = 1
                        print("Player Here")
                    elif rows[row][col] == "_":
                        rowSlice[col] = 0
                        print("Nothing Here")
                    elif rows[row][col] == "O":
                        rowSlice[col] = 2
                        print("I'm Here")
                        
                examinedBoard.append(rowSlice)
                print(examinedBoard)
                            
                    
                    
                #if (rows[0][num] == playerMark) and (rows[1][num] == playerMark) and (rows[2][num] == playerMark):
                 #   return(player)
            ## check for diagonals
            #if rows[1][1] == playerMark:
             #   if (rows[0][0] == playerMark) and (rows[2][2] == playerMark):
              #      return(player)
               # elif (rows[2][0] == playerMark) and (rows[0][2] == playerMark):
                #    return(player)     
            
    elif AI_Turn == False:
        while not done:
            #inputs
            while type(row) != int:
                answer = input('Indicate which row. ')
                if answer in '123':
                    row = int(answer)
                else:
                    print(answer, 'is an invalid row -- 1, 2 or 3 only')
                    
            while type(col) != int:
                answer = input('Indicate which column. ')
                if answer in '123':
                    col = int(answer)
                else:
                    print(answer, 'is an invalid row -- 1, 2 or 3 only')
                    
            ## check if same in a row
            row_list = rows[row-1]
            if row_list[col-1] == '_':
                row_list[col-1] = player
                done = True
            else:
                print('Row',row,'Column',col,'is already occupied. Please choose again.')
                row = False
                col = False
                
        ## print the board
        print('Game So Far')
        for row in rows:
            print(row)
            
            
        ## The rest of the code checks if any player has won
        for row_list in rows:
            if (row_list[0] == player) and (row_list[1]== player) and(row_list[2]==player):
                return(player)
        ## check if same in a column
        for num in range(3):
            if (rows[0][num] == player) and (rows[1][num] == player) \
               and (rows[2][num] == player):
                return(player)
        ## check for diagonals
        if rows[1][1] == player:
            if (rows[0][0] == player) and (rows[2][2] == player):
                return(player)
            elif (rows[2][0] == player) and (rows[0][2] == player):
                return(player)     

def tic_tac_toe():
    rows = []
    for num in range(3):
        row = ['_','_','_']
        rows.append(row)
    turns = 0
    player = 'X'
    win = False
    AI_Turn = False
    firstTurn = True
    secondTurn = False
    while (not win) and (turns<9):
        if player == 'X':
            player = 'O'
            AI_Turn = True
            if turns == 0:
                firstTurn = True
            elif turns == 2:
                firstTurn = False
                secondTurn = True
            elif turns >= 4:
                firstTurn = False
                secondTurn = False
                
        else:
            player = 'X'
            AI_Turn = False 
        win = go_tic_tac_toe_turn(player,rows,AI_Turn,firstTurn,secondTurn)
        turns = turns+1
    if win in ['X','O']:
        print(player+' wins!!!!!!')
    else:
        print('It is a draw!!!!!')
        
        
def tic_tac_AI():
    row_selection = 0
    
    return(row_selection)
        
tic_tac_toe()
