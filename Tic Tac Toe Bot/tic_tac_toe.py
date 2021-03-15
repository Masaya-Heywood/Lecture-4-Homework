import turtle
import random
import sys

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
            
            print_AI_move(rows)
                
        elif secondTurn == True:
            #row_list = rows[[2][0]]
            if rows[1][1] == '_':
                rows[1][1] = player
            else:
                while not done:
                    moveSelector = random.randint(0,len(bestMoves)-1)
        
                    row_list = rows[bestMoves[moveSelector][0]]
                    if row_list[bestMoves[moveSelector][1]] == '_':
                        row_list[bestMoves[moveSelector][1]] = player
                        done = True
            
            print_AI_move(rows)
        elif firstTurn != True and secondTurn != True:            
            #examine the board          
            examinedBoard = []
            for row in range(0,len(rows)):
                rowSlice = [None] * len(rows)
                #print(rowSlice)
                
                for col in range(0,len(rows)):
                    if rows[row][col] == playerMark:
                        rowSlice[col] = 1
                        #print("Player Here")
                    elif rows[row][col] == "_":
                        rowSlice[col] = 0
                        #print("Nothing Here")
                    elif rows[row][col] == "O":
                        rowSlice[col] = -1
                        #print("I'm Here")
                
                examinedBoard.append(rowSlice)
                        
            #arithmetic for reading the board
            rowSums = [None] * len(examinedBoard)
            colSums = [None] * len(examinedBoard)
            count = 0
            for row in examinedBoard:
                rowSums[count] = sum(row)
                count += 1
            
            count = 0
            for cols in range(0,len(examinedBoard)):
                colSums[count] = examinedBoard[0][cols] + examinedBoard[1][cols] + examinedBoard[2][cols]
                count += 1
                
            #attempting to win or block player
            finished = False
            dimensionConditions = [False,False,False]
            #check rows
            breakBlock = False
            for row in rowSums: 
                if row == -2: #check the total of the row
                    colCount = -1
                    for each in rows[rowSums.index(row)]: #find the empty space
                        colCount += 1
                        if each == "_":
                            print("Row to Win", rowSums.index(row))
                            print("Col to Win", colCount)
                            print("PLacing at", rows[rowSums.index(row)][colCount])
                            rows[rowSums.index(row)][colCount] = player
                            print_AI_move(rows)
                            sys.exit("The AI scored a win!")
                            finished = True
                            
                elif row == 2:
                    colCount = -1
                    for each in rows[rowSums.index(row)]:
                        colCount += 1
                        if each == "_":
                            print("Row to block", rowSums.index(row))
                            print("Col to block", colCount)
                            print("PLacing at", rows[rowSums.index(row)][colCount])
                            rows[rowSums.index(row)][colCount] = player
                            finished = True
                        if breakBlock == True:
                            break
            
            #check columns
            breakBlock = False
            #for row in range(0,len(rows)):
            #   for col in range(0,len(rows)):
            for col in colSums:
                if col == -2: #check the total of the column
                    rowCount = -1
                    checkRows = 0
                    for each in rows[checkRows][colSums.index(col)]: #find the empty space
                        rowCount += 1
                        checkRows += 1
                        if each == "_":
                            print("(Column)Col to Win", colSums.index(col))
                            print("(Column)Row to Win", checkRows)
                            print("PLacing at", rows[colSums.index(col)][checkRows])
                            rows[checkRows][colSums.index(col)] = player
                            print_AI_move(rows)
                            sys.exit("The AI scored a win!")
                            finished = True
                            #check_by_columns = False
                            
                elif col == 2:
                    checkRows = 0
                    rowCount = -1
                    for each in rows[checkRows][colSums.index(col)]: #find the empty space
                        rowCount += 1
                        checkRows += 1
                        if each == "_":
                            print("(Column)Col to Block", colSums.index(col))
                            print("(Column)Row to Block", rowCount)
                            print("PLacing at", rows[rowCount][colSums.index(col)])
                            rows[rowCount][colSums.index(col)] = player
                            finished = True
                            breakBlock = True
                            #check_by_columns = False
                        if breakBlock == True:
                            break
                        
                #check diagonals win
            while not finished:
                if rows[1][1] == player:
                    if (rows[0][0] == player) or (rows[2][2] == player):
                        if rows[0][0] == "_":
                            rows[0][0] = player
                            print_AI_move(rows)
                            check_win(rows, player)
                            finished = True
                        elif rows[2][2] == "_":
                            rows[2][2] = player
                            print_AI_move(rows)
                            check_win(rows, player)
                            finished = True
                            
                    #alternate diagonals
                    if (rows[2][0] == player) or (rows[0][2] == player):
                        if rows[2][0] == "_":
                            rows[2][0] = player
                            print_AI_move(rows)
                            check_win(rows, player)
                            finished = True
                        elif rows[2][2] == "_":
                            rows[0][2] = player
                            print_AI_move(rows)
                            check_win(rows, player)
                            finished = True
                            
                elif rows[1][1] == "X":
                    if (rows[0][0] == "X") or (rows[2][2] == "X"):
                        if rows[0][0] == "_":
                            rows[0][0] = player
                            finished = True
                            print("Player has diag to block")
                        elif rows[2][2] == "_":
                            print("Player has diag to block")
                            rows[2][2] = player
                            finished = True
                            
                    #alternate diagonals
                    if (rows[2][0] == "X") or (rows[0][2] == "X"):
                        if rows[2][0] == "_":
                            print("Player has diag to block")
                            rows[2][0] = player
                            finished = True
                        elif rows[0][2] == "_":
                            print("Player has diag to block")
                            rows[0][2] = player
                            finished = True

                else:                                  
                    #do a random move if nothing else can be done
                    while not finished: #incase no wins or blocks can be achieved
                        row = random.randint(0,2)
                        col = random.randint(0,2)
            
                        row_list = rows[row][col]
                        if rows[row][col] == '_':
                            rows[row][col] = player
                            print("You likley have reached too far")
                            finished = True
                    
            print_AI_move(rows)
                
            
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
        go_tic_tac_toe_turn(player,rows,AI_Turn,firstTurn,secondTurn)
        turns = turns+1
    if win in ['X','O']:
        print(player+' wins!!!!!!')
    else:
        print('It is a draw!!!!!')
        
        
def tic_tac_AI():
    row_selection = 0
    
    return(row_selection)


def print_AI_move(rows):
    print("AI's Move")
    for row in rows:
        print("AI", row)
    return()

def check_win(rows, player):
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
            sys.exit("The AI scored a win!")
        elif (rows[2][0] == player) and (rows[0][2] == player):
            sys.exit("The AI scored a win!")  
        
tic_tac_toe()
